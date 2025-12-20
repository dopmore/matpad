import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()


PINS = [board.D26, board.D29, board.D2, board.D27, board.D6, board.D4, board.D28, board.D3]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)


keyboard.keymap = [
    [KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N9]
]

encoder_handler.pins = ((board.GP1, board.GP0, board.GP7))

Zoom_in = KC.LCTRL(KC.EQUAL)
Zoom_out = KC.LCTRL(KC.MINUS)

encoder_handler.map = [ (Zoom_in, Zoom_out, KC.MUTE) ]

if __name__ == '__main__':
    keyboard.go()