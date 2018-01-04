#!/usr/bin/env python3
import json
import time

import autopy3
import keyboard


def print_banner():
    print('')
    print('===============================================================================================')
    print('With this program you can register a scan scenario which will be repeated at specified interval')
    print('===============================================================================================')
    print('')


SCENARIO = []

# TODO: use globals()
continue_loop = True


def watch_mouse_position():
    while continue_loop:
        mouse_pos = autopy3.mouse.get_pos()
        print(mouse_pos)
        SCENARIO.append(mouse_pos)
        time.sleep(0.6)


def stop_loop():
    print('Stop and export')
    continue_loop = False


def on_new_click():
    mouse_pos = autopy3.mouse.get_pos()
    print('Click=', mouse_pos)
    SCENARIO.append('Click=' + str(mouse_pos[0]) + ',' + str(mouse_pos[1]))


def register_hot_keys():
    keyboard.add_hotkey('a', lambda: on_new_click())
    keyboard.add_hotkey('ctrl+q', lambda: stop_loop())


def export_json():
    f = open('scenario.json', 'w')
    json.dumps(SCENARIO, f)


if __name__ == "__main__":
    print_banner()
    register_hot_keys()
    watch_mouse_position()
    export_json()
