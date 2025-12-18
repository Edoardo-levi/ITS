#!/bin/bash
# create_lab_netns.sh
# Crea tre network namespaces (nsA, nsB, nsM) collegate a un bridge L2 (brlab).
# Uso: sudo ./create_lab_netns.sh
set -euo pipefail

if [ "$(id -u)" -ne 0 ]; then
  echo "Devi eseguire questo script come root (sudo)."
  exit 1
fi

# CONFIGURAZIONE (modifica se vuoi)
NS_A="nsA"
NS_B="nsB"
NS_M="nsM"
BRIDGE="brlab"

VETH_A="vethA"
VETH_A_PEER="vethA-peer"
VETH_B="vethB"
VETH_B_PEER="vethB-peer"
VETH_M="vethM"
VETH_M_PEER="vethM-peer"

IP_A="10.10.10.10/24"
IP_B="10.10.10.50/24"
IP_M="10.10.10.200/24"
GATEWAY="10.10.10.1/24"

# helper per safe-delete
safe_ip() {
  ip netns del "$1" 2>/dev/null || true
}

safe_link_del() {
  ip link del "$1" 2>/dev/null || true
}

# cleanup iniziale parziale (non troppo aggressivo)
safe_ip "${NS_A}"
safe_ip "${NS_B}"
safe_ip "${NS_M}"
safe_link_del "${BRIDGE}"

echo "[*] Creazione bridge ${BRIDGE}"
ip link add name "${BRIDGE}" type bridge || true
ip link set "${BRIDGE}" up
# assegna gateway IP al bridge (opzionale, utile per default routes)
ip addr add "${GATEWAY}" dev "${BRIDGE}" 2>/dev/null || true

echo "[*] Creazione namespaces: ${NS_A}, ${NS_B}, ${NS_M}"
ip netns add "${NS_A}"
ip netns add "${NS_B}"
ip netns add "${NS_M}"

echo "[*] Creazione veth pairs e collegamento al bridge"

# A
ip link add "${VETH_A}" type veth peer name "${VETH_A_PEER}"
ip link set "${VETH_A}" master "${BRIDGE}"
ip link set "${VETH_A}" up
ip link set "${VETH_A_PEER}" netns "${NS_A}"
ip netns exec "${NS_A}" ip link set "${VETH_A_PEER}" name eth0
ip netns exec "${NS_A}" ip addr add "${IP_A}" dev eth0
ip netns exec "${NS_A}" ip link set eth0 up
ip netns exec "${NS_A}" ip route add default via "${GATEWAY%/*}" || true

# B
ip link add "${VETH_B}" type veth peer name "${VETH_B_PEER}"
ip link set "${VETH_B}" master "${BRIDGE}"
ip link set "${VETH_B}" up
ip link set "${VETH_B_PEER}" netns "${NS_B}"
ip netns exec "${NS_B}" ip link set "${VETH_B_PEER}" name eth0
ip netns exec "${NS_B}" ip addr add "${IP_B}" dev eth0
ip netns exec "${NS_B}" ip link set eth0 up
ip netns exec "${NS_B}" ip route add default via "${GATEWAY%/*}" || true

# M
ip link add "${VETH_M}" type veth peer name "${VETH_M_PEER}"
ip link set "${VETH_M}" master "${BRIDGE}"
ip link set "${VETH_M}" up
ip link set "${VETH_M_PEER}" netns "${NS_M}"
ip netns exec "${NS_M}" ip link set "${VETH_M_PEER}" name eth0
ip netns exec "${NS_M}" ip addr add "${IP_M}" dev eth0
ip netns exec "${NS_M}" ip link set eth0 up
ip netns exec "${NS_M}" ip route add default via "${GATEWAY%/*}" || true

echo "[+] Setup completato."
echo ""
echo "Controlli utili:"
echo "  ip link show ${BRIDGE}"
echo "  ip netns list"
echo ""
echo "Per entrare nelle namespace:"
echo "  sudo ip netns exec ${NS_A} bash   # shell in A"
echo "  sudo ip netns exec ${NS_B} bash   # shell in B"
echo "  sudo ip netns exec ${NS_M} bash   # shell in M"
echo ""
echo "Esempi rapidi:"
echo "  sudo ip netns exec ${NS_A} ip addr show"
echo "  sudo ip netns exec ${NS_A} ping -c 2 ${IP_B%/*}"
echo ""
echo "Se vuoi cancellare tutto: esegui cleanup_lab_netns.sh (fornisco lo script separato)."
