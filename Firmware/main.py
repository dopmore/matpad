from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation, MatrixScanner
from kmk.modules.rotary import RotaryEncoderModule
from kmk.extensions.media_keys import MediaKeys

import board
from kmk.modules.rotary import RotaryEncoder

keyboard = KMKKeyboard()


cols = [board.D26, board.D27, board.D28]
rows = [board.D29, board.D6, board.D7, board.D0]

scanner = MatrixScanner(
    row_pins=rows,
    col_pins=cols,
    diode_orientation=DiodeOrientation.COL2ROW
)
keyboard.modules.append(scanner)


keyboard.extensions.append(MediaKeys())


encoder = RotaryEncoder(
    pins=(board.D2, board.D1),
    clockwise=MediaKeys.volume_up,
    counter_clockwise=MediaKeys.volume_down,
    button=board.D4,
    button_key=KC.KP_ENTER 
)
keyboard.modules.append(encoder)


keyboard.keymap = [
    [
        [KC.DOT, KC.PLUS, KC.KP_ENTER],    # ROW1
        [KC.KP_1, KC.KP_2, KC.KP_3],    # ROW2
        [KC.KP_4, KC.KP_5, KC.KP_6],    # ROW3
        [KC.KP_7, KC.KP_8, KC.KP_9],    # ROW4
    ]
]

if __name__ == '__main__':
    keyboard.go()
