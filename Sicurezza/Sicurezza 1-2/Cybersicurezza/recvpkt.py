from scapy.all import sniff, Ether, get_if_hwaddr

IFACE = "tap0"                       # interfaccia da monitorare
MY_MAC = get_if_hwaddr(IFACE).lower()  # MAC locale

def handle(pkt):
    if Ether in pkt and pkt[Ether].dst.lower() == MY_MAC:
        print("Pacchetto ricevuto per me:", pkt.summary())
        pkt.show()

# sniffa solo 1 pacchetto (count=1), con filtro Python
sniff(iface=IFACE, prn=handle, lfilter=lambda p: Ether in p and p[Ether].dst.lower() == MY_MAC, count=1)
