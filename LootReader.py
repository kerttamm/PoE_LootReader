# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 09:57:38 2023
Path of Exile, loot highlight script
@author: Kert Tamm, kerttamm66@gmail.com
"""

import time
import pygetwindow as gw
import pynput
import tkinter as tk
import win32clipboard
import winsound
import gc
from pynput.keyboard import Key, Controller, Listener, KeyCode
#from pynput.mouse import Controller
#mouse = pynput.mouse.Controller()
#mouse.position
keyboard = pynput.keyboard.Controller()
time_pressed = time.time()


# open good_mods.txt and save the lines to list
# each line in the file is the string to be fulfilled to highlight an item
with open('good_mods.txt') as f:
     good_mods = f.readlines()
     
def process_item():
    # get item from the clippboard
    try:
        win32clipboard.OpenClipboard()
        item = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        # print(item.strip()) # uncomment for debugging
    except:
        item = ""
    # check the item against the list of desired mods
    i=0
    while i<len(good_mods):
        if good_mods[i].strip() in item.strip():
            # print(["good item",good_mods[i].strip()]) # uncomment to spam terminal why its good item
            frequency = 500; duration = 66;
            # Make beep sound on Windows for good stuff
            winsound.Beep(frequency, duration)
        i=i+1

def process_key(key):
    # only chek every 100 ms interval
    global time_pressed
    if (time.time() - time_pressed > 0.1):
        time_pressed = time.time()
    else:
        return    
    #ignore key press when PoE is not the active window
    if gw.getActiveWindow().title != "Path of Exile":
        # print("PoE window not in focus!") # for debugging
        return
    if key == Key.ctrl_l:
        # press and release cltr+c to make copy of the item to clipboard
        #keyboard.press(Key.ctrl_l)
        keyboard.press('c')
        keyboard.release('c')
        #keyboard.release(Key.ctrl_l)
        # print("ctrl + c has been pressed") # for debugging
        gc.collect() # force garbage collection to avoid "threads" error later
        # call function to process the item from clipboard
        process_item()
        
def start_mods_detector():
    global listener
    # Activate listener which will call process_key function every time key is pressed
    listener = Listener(on_press = process_key)
    listener.start()

def stop_mods_detector():
    listener.stop()
    
########################### ui part ##############################

root= tk.Tk()
canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()
running = False

def toggle_mod_detector():  
    global running

    label1 = tk.Label(root, text= 'Script is running!', fg='blue', font=('helvetica', 12, 'bold'))
    label2 = tk.Label(root, text= 'Script is stopped!', fg='red', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window= label2 if running else label1)
   
    if running:
        stop_mods_detector()
    else:
        start_mods_detector()
    running = not running

def main():
    button1 = tk.Button(text='Toggle the script', command=toggle_mod_detector, bg='brown',fg='white')
    canvas1.create_window(150, 150, window=button1)
    root.title("PoE LootReader script")
    root.mainloop()

if __name__ == "__main__":
    main()