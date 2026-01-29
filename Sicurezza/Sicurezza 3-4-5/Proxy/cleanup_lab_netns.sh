#!/bin/bash
# cleanup_lab_netns.sh
# Rimuove namespaces e bridge creati dallo script create_lab_netns.sh
# Uso: sudo ./cleanup_lab_netns.sh
set -euo pipefail

if [ "$(id -u)" -ne 0 ]; then
  echo "Devi eseguire questo script come root (sudo)."
  exit 1
fi

NS_A="nsA"
NS_B="nsB"
NS_M="nsM"
BRIDGE="brlab"

VETH_A="vethA"
VETH_B="vethB"
VETH_M="vethM"

echo "[*] Arresto e pulizia namespaces e interfacce..."

# rimuovi namespaces (safe)
ip netns del "${NS_A}" 2>/dev/null || true
ip netns del "${NS_B}" 2>/dev/null || true
ip netns del "${NS_M}" 2>/dev/null || true

# rimuovi bridge e eventuali veth rimasti
ip link set "${BRIDGE}" down 2>/dev/null || true
ip link del "${BRIDGE}" 2>/dev/null || true

# tenta rimozione veth residui (se esistono nella root netns)
ip link del "${VETH_A}" 2>/dev/null || true
ip link del "${VETH_B}" 2>/dev/null || true
ip link del "${VETH_M}" 2>/dev/null || true

echo "[+] Pulizia completata."

