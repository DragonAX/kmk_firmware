print("Starting")

import board
from storage import getmount
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType, SplitSide

side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT

keyboard = KMKKeyboard()
split = Split(split_side=None,
              data_pin2=board.GP0,
              data_pin=board.GP1,
              uart_flip=False
        )
keyboard.modules.append(split)

if side == SplitSide.RIGHT:
    keyboard.col_pins = (
            board.GP4,
            board.GP9, 
            board.GP10, 
            board.GP3, 
            board.GP7, 
            board.GP2,)
    keyboard.row_pins = (
            board.GP21, 
            board.GP20, 
            board.GP19, 
            board.GP18, 
            board.GP17)
else:
    keyboard.col_pins = (
            board.GP2, 
            board.GP7, 
            board.GP3, 
            board.GP4, 
            board.GP5, 
            board.GP8,)
    keyboard.row_pins = (
            board.GP6, 
            board.GP9, 
            board.GP21, 
            board.GP20, 
            board.GP15)


keyboard.diode_orientation = DiodeOrientation.COL2ROW

        # HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----#ENCODER--#ENCODER--# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----

XXXXXXX = KC.NO
keyboard.keymap = [
    [# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
     XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  
     KC.QUOTE, KC.COMMA, KC.DOT,   KC.P,     KC.Y,     XXXXXXX,  KC.F,     KC.G,     KC.C,     KC.R,     KC.L,     KC.SLASH,
     KC.A,     KC.O,     KC.E,     KC.U,     KC.I,     XXXXXXX,  KC.D,     KC.H,     KC.T,     KC.N,     KC.S,     KC.MINUS,
     KC.SCOLON,KC.Q,     KC.J,     KC.K,     KC.X,     XXXXXXX,  KC.B,     KC.M,     KC.W,     KC.V,     KC.Z,     KC.BSLASH,
     KC.LCTRL, KC.LGUI,  KC.LALT,  KC.ENTER, KC.LSHIFT,KC.TAB,   KC.BKDL,  KC.SPACE, KC.RALT,  KC.RGUI,  KC.RCTL,  XXXXXXX,
     ],
]



if __name__ == '__main__':
    keyboard.go()
