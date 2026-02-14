import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler

# Pinout
COL1 = board.D0
COL2 = board.D1
COL3 = board.D2
COL4 = board.D10
ROW1 = board.D3
ROW2 = board.D4
ROW3 = board.D5
ROW4 = board.D6
PUSHBUTTON = board.D9
ROTA = board.D8
ROTB = board.D7


keyboard = KMKKeyboard()

# Basic matrix settings
keyboard.col_pins = (COL1, COL2, COL3, COL4)
keyboard.row_pins = (ROW1, ROW2, ROW3, ROW4)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.extensions.append(MediaKeys())

# Encoder settings
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((ROTA, ROTB, PUSHBUTTON, False),)
encoder_handler.map = (((KC.VOLD, KC.VOLU, KC.KP_ENTER),),)

# Keymap
keyboard.keymap = [[
        # 16 matrix keys (row-major order)
        KC.KP_1, KC.KP_2, KC.KP_3, KC.NUMLOCK,
        KC.KP_4, KC.KP_5, KC.KP_6, KC.KP_ASTERISK,
        KC.DOT,  KC.KP_0, KC.KP_PLUS, KC.KP_ENTER,
        KC.KP_7, KC.KP_8, KC.KP_9, KC.KP_MINUS,
        
        

        # Encoder virtual keys (MUST exist even if mapped elsewhere)
        KC.VOLD,   # encoder CCW
        KC.VOLU,   # encoder CW
        KC.MUTE,   # encoder button
        ]
]


if __name__ == '__main__':
    keyboard.go()