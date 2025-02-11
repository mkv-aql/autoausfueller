
import pyautogui
import time
import pyperclip
import keyboard

special_characters = ['ä','ö','ü','ß', 'Ä', 'Ö', 'Ü']
example_text = "Hellüki"
example_text_2 = "Hellolol"
example_text_3 = "HellÄ"

def paste_umlaut(char):
    pyperclip.copy(char)
    out = pyperclip.paste()
    print(out)
    return out

def umlaut_detect_input(string):

    for char in string:
        if char in special_characters:
            print("yes ", char)
            result = string.split(f'{char}')
            print(result)
            pyperclip.copy(char)
            out = pyperclip.paste()
            print(out)
            return True
    print("No")
    return False

if __name__ == "__main__":
    time.sleep(1)
    pyautogui.move(-500, 0, duration = 0.5)
    time.sleep(1)
    pyautogui.click()

    umlaut_detect_input(example_text)
    umlaut_detect_input(example_text_2)
    umlaut_detect_input(example_text_3)

    pyautogui.write(example_text)  # write the value and covers more letters
    pyautogui.write(example_text_2)  # write the value and covers more letters
    pyautogui.typewrite('ü')  # write the value and covers more letters

    keyboard.write('Ö')
    keyboard.write('Ökologie')


