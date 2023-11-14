# PoE_LootReader
Path of Exile lootreader script. Beeps if sees good mod on ctrl+mouse over.

Inspired partly by Path of Exile mods_detector script https://github.com/Nathaniell1/mods_detector

The script checks all lines in the file good_mods.txt against an item when the left ctrl key is held down and makes a Windows "beep" sound if the match is found so that you know to read the item in question. If multiple lines are matched it does multiple beeps in rapid order (i.e., an item that has for example three "good_mods" will do three beeps in rapid order).

The script opens a separate small window where there is a toggle button allowing you to switch the mod-checking script on and off without having to stop the entire script.

The script does not work with PoE in full-screen mode, only a windowed or borderless window. 

Initially written on Anaconda 3 Python environment using SPyder IDE 5.4.3 Python 3.9.18 64-bit | Qt 5.15.2 | PyQt5 5.15.7 | Windows 10

pygetwindow and pynput packages had to be installed separately under conda
