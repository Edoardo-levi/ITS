from scapy.all import Ether, Raw, sendp

def send_with_scapy(iface, dst_mac, src_mac, ethertype, payload, count=1):
    pkt = Ether(dst=dst_mac, src=src_mac, type=ethertype) / Raw(load=payload)
    sendp(pkt, iface=iface, count=count, verbose=True)

if __name__ == "__main__":
    iface = "tap0"
    dst_mac = "00:11:22:33:44:27"
    src_mac = "00:11:22:33:44:15"
    ethertype = 0x88B5
    payload = b"Hello from Scapy"
    send_with_scapy(iface, dst_mac, src_mac, ethertype, payload)
