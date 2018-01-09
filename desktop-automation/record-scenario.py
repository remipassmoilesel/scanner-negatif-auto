#!/usr/bin/env python3
import json
import time

import autopy3
import keyboard


# TODO: watch keys ?

class RecordType:
    Click = 'Click'
    Move = 'Move'
    Key = 'Key'


def print_banner():
    print('')
    print('===============================================================================================')
    print('With this program you can register a scan scenario which will be repeated at specified interval')
    print('===============================================================================================')
    print('')


json_data = []

continue_loop = True


def watch_mouse_position():
    global continue_loop
    global json_data

    while continue_loop:
        mouse_pos = autopy3.mouse.get_pos()
        register_position(RecordType.Move, mouse_pos)
        time.sleep(0.6)


def stop_loop():
    global continue_loop

    print('Stop and export')
    continue_loop = False


def on_new_click():
    global json_data

    mouse_pos = autopy3.mouse.get_pos()
    register_position(RecordType.Click, mouse_pos)


def register_hot_keys():
    keyboard.add_hotkey('a', lambda: on_new_click())
    keyboard.add_hotkey('ctrl+q', lambda: stop_loop())


def export_json():
    global json_data

    f = open('scenario.json', 'w')
    json.dump(json_data, f)


def register_position(prefix, pos):
    pos_str = [prefix, pos[0], pos[1]]
    print(pos_str)
    json_data.append(pos_str)


if __name__ == "__main__":
    print_banner()
    register_hot_keys()
    watch_mouse_position()
    export_json()
