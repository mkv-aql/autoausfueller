__author__ = 'mkv-aql'

import matplotlib as mp
import tkinter as tk
import os
import pywinauto
import pygetwindow as gw
import class_autoausfueller as aa
import threading


fetch = []


# Inside window function
def window(root):
    # Create and organize the labels and entries
    labels_and_entries = [
        ("Straße", "Juliusstraße"),
        ("Hausnummer", "0"),
        ("PLZ", "65428"),
        ("Ort", "Rüsselsheim am Main"),
        ("Ortsteil 1", "Eselswiese"),
        ("Ortsteil 2", "Eselswiese"),
        ("Wohneinheiten (Privat)", "1"),
        ("Wohneinheiten (Geschäftlich)", "0"),
        ("Anmerkungen", "")
        # ("Baulücke", "0")
    ]

    entries = []
    for label_text, default_value in labels_and_entries:
        label = tk.Label(root, text=label_text)
        label.pack()
        entry = tk.Entry(root)
        entry.pack()
        entry.insert(0, default_value)
        entries.append(entry)

    # Initialize fetch with default values
    fetch = [entry.get() for entry in entries]

    def refresh():
        """Updates the fetch list with the latest entry values."""
        nonlocal fetch
        fetch = [entry.get() for entry in entries]
        print(f"Updated fetch: {fetch}")

    def next():
        """Increments the Hausnummer (second entry) by 2."""
        try:
            current_number = int(entries[1].get())
        except ValueError:
            current_number = 0
        entries[1].delete(0, tk.END)
        entries[1].insert(0, str(current_number + 1))
        refresh()

    def prev():
        """Increments the Hausnummer (second entry) by 2."""
        try:
            current_number = int(entries[1].get())
        except ValueError:
            current_number = 0
        entries[1].delete(0, tk.END)
        entries[1].insert(0, str(current_number - 1))
        refresh()

    def insert_data():
        """Calls the insert function with the latest fetch data."""
        refresh()
        insert(fetch, tick_var.get())

    def bauluecke_check():
        if tick.get() == 1:
            print("Baulücke")
            fetch.append("1")
        else:
            print("Keine Baulücke")
            fetch.append("0")

    # tick box
    # checkbox_var = tk.IntVar()  # 0 = unchecked, 1 = checked
    tick_var = tk.IntVar()  # 0 = unchecked, 1 = checked
    tick = tk.Checkbutton(root, text="Baulücke", variable=tick_var).pack()


    # Buttons
    button0 = tk.Button(root, text="+1 Haus Nr.", command=next)
    # button0.pack()
    button0.pack(side=tk.LEFT)

    button1 = tk.Button(root, text="-1 Haus Nr.", command=prev)
    # button1.pack()
    button1.pack(side=tk.LEFT)

    # button0.grid(column=0, row=0)  # grid dynamically divides the space in a grid
    # button1.grid(column=1, row=0)  # and arranges widgets accordingly

    # button0.pack(side=tk.LEFT)  # pack starts packing widgets on the left
    # button1.pack(side=tk.LEFT)  # and keeps packing them to the next place available on the left

    button2 = tk.Button(root, text="Update", command=refresh)
    button2.pack()

    button3 = tk.Button(root, text="Insert", command=insert_data)
    button3.pack()


def insert(fetch, tick_var):
    print(f'\nFetched data:\n{fetch}\n')
    # Open images
    # step1 = cv2.imread('weiter.JPG', cv2.IMREAD_UNCHANGED)
    # Display images
    #cv2.imshow('Image', step1)

    # goto()

    # go to microsoft edge window
    # os.system("start msedge")
    # go to the opened tab
    # os.system("start msedge https://www.google.com")

    # entry = tk.Entry(root)
    # entry.pack()

    # if the tick box is ticked, print ticked

    if tick_var == 1:
        aa.bauluecke_status = 1
        print("Baulücke checkbox is ticked!")
    else:
        aa.bauluecke_status = 0
        print("Baulücke checkbox is not ticked.")

    aa.dict = {
        "strasse": fetch[0],
        "hausnummer": fetch[1],
        "plz": fetch[2],
        "ort": fetch[3],
        "ortsteil1": fetch[4],
        "ortsteil2": fetch[5],
        "we_privat": fetch[6],
        # "bauluecke": fetch[7],
    }

    aa.run()



# def goto():
#     windows = gw.getWindowsWithTitle('msedge.exe')
#
#     if windows:
#         # Focus on the first window with the title
#         window = windows[0]
#         window.activate()
#
#         # You might need to use pywinauto to interact further
#         app = pywinauto.Application().connect(handle=window._hWnd)
#         browser = app.window(handle=window._hWnd)
#         browser.set_focus()
#     else:
#         print("No window found with the specified title.")


# Tkinter window
root = tk.Tk()
root.title("Automatisches Ausfüllen")
root.geometry("400x550") # Window size
root.geometry("+1300+250") # Window position
# Keep window above everything
root.attributes("-topmost", True)
window(root)

# root.mainloop()

# thread 1 for tkinter window
t1 = threading.Thread(target=root.mainloop())

t1.start()

