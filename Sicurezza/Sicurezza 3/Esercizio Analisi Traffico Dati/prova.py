import re
from datetime import datetime
from collections import defaultdict

# -------------------------
# CONFIG
# -------------------------
FILE = "traffico_http.txt"

# regex per identificare timestamp
TS_RE = re.compile(r"(\d{2}:\d{2}:\d{2}\.\d+)")

# GET
GET_RE = re.compile(r"GET\s+([\/\w\.\-\_]+)\s+HTTP")

# Risposta server
RESP_RE = re.compile(r"HTTP\/1\.[01]\s+(\d{3})")

# Estrazione porta di flusso (es: proxy.60482)
FLOW_RE = re.compile(r"proxy\.(\d+)")


# --------------------------------------------------------
# PARSING
# --------------------------------------------------------

requests = {}              # flow_id → {url, ts_req}
responses = {}             # flow_id → {status, ts_resp}
visit_counter = defaultdict(int)
logs_per_site = defaultdict(list)
response_times = defaultdict(list)


def parse_timestamp(line):
    m = TS_RE.search(line)
    if not m:
        return None
    return datetime.strptime(m.group(1), "%H:%M:%S.%f")


with open(FILE, "r") as f:
    for line in f:
        ts = parse_timestamp(line)
        if not ts:
            continue

        # estrai flow
        flow_match = FLOW_RE.search(line)
        if not flow_match:
            continue

        flow_id = flow_match.group(1)

        # --------------------------
        # MATCH GET
        # --------------------------
        get_m = GET_RE.search(line)
        if get_m:
            url = get_m.group(1)
            requests[flow_id] = {
                "url": url,
                "ts_req": ts
            }
            continue

        # --------------------------
        # MATCH RESPONSE
        # --------------------------
        resp_m = RESP_RE.search(line)
        if resp_m:
            code = int(resp_m.group(1))
            responses[flow_id] = {
                "status": code,
                "ts_resp": ts
            }
            continue


# --------------------------------------------------------
# ASSOCIAZIONE RICHIESTE ↔ RISPOSTE
# --------------------------------------------------------

for flow_id, req in requests.items():
    if flow_id not in responses:
        continue

    resp = responses[flow_id]

    url = req["url"]
    status = resp["status"]
    t_req = req["ts_req"]
    t_resp = resp["ts_resp"]
    delta = (t_resp - t_req).total_seconds() * 1000  # ms

    visit_counter[url] += 1
    response_times[url].append(delta)

    logs_per_site[url].append(
        f"{t_req} → {t_resp}  |  {delta:.2f} ms  |  status={status}"
    )


# --------------------------------------------------------
# OUTPUT FINALE
# --------------------------------------------------------

print("\n===== TOP 10 SITI VISITATI =====")
top_10 = sorted(visit_counter.items(), key=lambda x: x[1], reverse=True)[:10]
for url, count in top_10:
    print(f"{url}: {count} visite")

print("\n===== TEMPI MEDI DI RISPOSTA =====")
for url, times in response_times.items():
    avg = sum(times) / len(times)
    print(f"{url}: {avg:.2f} ms")

print("\n===== LOG PER SITO (per analisi DoS) =====")
for url, entries in logs_per_site.items():
    print(f"\n--- {url} ---")
    for entry in entries:
        print(entry)