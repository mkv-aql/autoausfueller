__author__ = 'mkv-aql'

import cv2
import matplotlib as mp
import tkinter as tk
import os
import pywinauto
import pygetwindow as gw
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        entries[1].insert(0, str(current_number + 2))
        refresh()

    def insert_data():
        """Calls the insert function with the latest fetch data."""
        refresh()
        insert(fetch.copy())

    # Buttons
    button = tk.Button(root, text="+2 Haus Nr.", command=next)
    button.pack()

    button2 = tk.Button(root, text="Update", command=refresh)
    button2.pack()

    button3 = tk.Button(root, text="Insert", command=insert_data)
    button3.pack()


def insert(fetch):

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

    aa.dict = {
        "strasse": fetch[0],
        "hausnummer": fetch[1],
        "plz": fetch[2],
        "ort": fetch[3],
        "ortsteil1": fetch[4],
        "ortsteil2": fetch[5],
        "we_privat": fetch[6]
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
root.title("Hello World")
root.geometry("300x400")
# Keep window above everything
root.attributes("-topmost", True)
window(root)

# root.mainloop()

# thread 1 for tkinter window
t1 = threading.Thread(target=root.mainloop())

t1.start()

