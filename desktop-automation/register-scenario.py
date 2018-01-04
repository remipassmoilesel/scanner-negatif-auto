#!/usr/bin/env python3
import autopy3
import time
import keyboard

def print_banner():
    print('')
    print('===============================================================================================')
    print('With this program you can register a scan scenario which will be repeated at specified interval')
    print('===============================================================================================')
    print('')

def watch_mouse_position():
    while True:
        print(autopy3.mouse.get_pos())
        time.sleep(0.6)

def on_new_click():
    print('Click=', autopy3.mouse.get_pos())

def register_hot_key():
    keyboard.add_hotkey('a', lambda: on_new_click())

if __name__ == "__main__":
    print_banner()
    register_hot_key()
    watch_mouse_position()
