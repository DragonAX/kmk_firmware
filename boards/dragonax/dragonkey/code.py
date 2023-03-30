print("Starting")

import board
from storage import getmount
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.modules.modtap import ModTap
from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys


modtap = ModTap()
# optional: set a custom tap timeout in ms
# modtap.tap_time = 300

side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT

split = Split(split_side=None,
              data_pin2=board.GP0,
              data_pin=board.GP1,
              uart_flip=False
        )

keyboard = KMKKeyboard()

keyboard.modules.append(split)
keyboard.modules.append(modtap)
keyboard.modules.append(Layers())
keyboard.modules.append(MouseKeys())

if side == SplitSide.RIGHT:
    keyboard.col_pins = (
            board.GP4,
            board.GP9, 
            board.GP10, 
            board.GP3, 
            board.GP7,  
            board.GP2,
            board.GP26,
            board.GP22)
    keyboard.row_pins = (
            board.GP21, 
            board.GP20,  
            board.GP19, 
            board.GP18, 
            board.GP17)
else:
    keyboard.col_pins = (
            board.GP8,
            board.GP5,
            board.GP4,
            board.GP3,
            board.GP7,
            board.GP2,
            board.GP10,
            board.GP11)
    keyboard.row_pins = (
            board.GP6, 
            board.GP9, 
            board.GP21, 
            board.GP20, 
            board.GP15)


keyboard.diode_orientation = DiodeOrientation.COL2ROW

        # HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----#ENCODER--#ENCODER--# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----

BASE_LAYER = 0
RAISED_LAYER = 1
XXXXXXX = KC.NO

SPC_RAISE = KC.LT(RAISED_LAYER, KC.SPACE, prefer_hold=True, tap_time=175)

keyboard.keymap = [
     # BASE_LAYERS
    [# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
     KC.MW_UP, KC.MW_DN, KC.MS_LT, KC.MS_DN, KC.MS_UP, KC.MS_RT, XXXXXXX,  XXXXXXX,   XXXXXXX, XXXXXXX, KC.MB_LMB,KC.MB_MMB,KC.MB_RMB,XXXXXXX,  XXXXXXX,  XXXXXXX,  
     KC.BSLASH,KC.QUOTE, KC.COMMA, KC.DOT,   KC.P,     KC.Y,     XXXXXXX,  XXXXXXX,   XXXXXXX, XXXXXXX, KC.F,     KC.G,     KC.C,     KC.R,     KC.L,    KC.SLASH, 
     KC.GRAVE, KC.A,     KC.O,     KC.E,     KC.U,     KC.I,     XXXXXXX,  XXXXXXX,   XXXXXXX, XXXXXXX, KC.D,     KC.H,     KC.T,     KC.N,     KC.S,    KC.MINUS,  
     KC.LBRC,  KC.SCOLON,KC.Q,     KC.J,     KC.K,     KC.X,     XXXXXXX,  XXXXXXX,   XXXXXXX, XXXXXXX, KC.B,     KC.M,     KC.W,     KC.V,     KC.Z,    KC.RBRC,  
     KC.LGUI,  KC.LCTRL,   XXXXXXX, KC.LALT, KC.ENTER, KC.LSHIFT,XXXXXXX,  KC.ESC,    KC.ESC, KC.MO(RAISED_LAYER), KC.SPACE,KC.BSPC,  KC.TAB,   KC.RALT,  KC.RCTL, KC.RGUI,  
     ],
    # RAISED_LAYER
    [# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
     XXXXXXX,  XXXXXXX,  KC.LEFT,  KC.DOWN,  KC.UP,    KC.RIGHT,XXXXXXX,  XXXXXXX,XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX, XXXXXXX,   
     KC.BSLASH,KC.QUOTE, KC.COMMA, KC.DOT,   XXXXXXX,  XXXXXXX, XXXXXXX,  XXXXXXX,XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX, KC.SLASH,
     XXXXXXX,  KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,   XXXXXXX,  XXXXXXX,XXXXXXX, XXXXXXX, KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,   KC.EQL,
     XXXXXXX,  KC.EXLM,  KC.AT,    KC.HASH,  KC.DOLLAR,KC.PERC, XXXXXXX,  XXXXXXX,XXXXXXX, XXXXXXX, KC.CIRC,  KC.AMPR,  KC.ASTR,  KC.LPRN,  KC.RPRN, XXXXXXX,   
     KC.LGUI,  KC.LCTRL,   KC.LALT,  KC.TAB, KC.ENTER, KC.LSHIFT,XXXXXXX,XXXXXXX, XXXXXXX, XXXXXXX, SPC_RAISE,KC.BSPC,  KC.ESC,   KC.RALT,  KC.RCTL, KC.RGUI,   
     ],
]



if __name__ == '__main__':
    keyboard.go()
