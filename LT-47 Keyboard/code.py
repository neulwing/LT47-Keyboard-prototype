print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())
keyboard.modules.append(Layers())
keyboard.row_pins = (board.GP2,board.GP3,board.GP4,board.GP5)
keyboard.col_pins = (board.GP6,board.GP7,board.GP8,board.GP9,board.GP10,board.GP11,board.GP12,board.GP13,board.GP14,board.GP15,board.GP27,board.GP28,board.GP29)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
[
    KC.ESC,KC.Q,KC.W,KC.E,KC.R,KC.T,KC.Y,KC.U,KC.I,KC.O,KC.P,KC.SCLN,KC.BSPC,
    KC.TAB,KC.A,KC.S,KC.D,KC.F,KC.G,KC.H,KC.J,KC.K,KC.L,KC.QUOT,KC.NO,KC.ENTER,
    KC.LSFT,KC.Z,KC.X,KC.C,KC.V,KC.B,KC.B,KC.N,KC.M,KC.COMM,KC.DOT,KC.UP,KC.SLSH,
    KC.LCTL,KC.LGUI,KC.LALT,KC.NO,KC.SPC,KC.NO,KC.NO,KC.SPC,KC.MO(1),KC.NO,KC.LEFT,KC.DOWN,KC.RIGHT,
],

[
    KC.GRV,KC.N7,KC.N8,KC.N9,KC.MINS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.PSCR,KC.TRNS,KC.DEL,
    KC.TRNS,KC.N4,KC.N5,KC.N6,KC.EQL,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.LBRC,KC.RBRC,KC.TRNS,KC.BSLS,
    KC.TRNS,KC.N1,KC.N2,KC.N3,KC.TRNS,KC.TRNS,KC.TRNS,KC.MEDIA_STOP,KC.MUTE,KC.MPRV,KC.MNXT,KC.VOLU,KC.MPLY,
    KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.N0,KC.TRNS,KC.TRNS,KC.MO(2),KC.TRNS,KC.TRNS,KC.HOME,KC.VOLD,KC.END,
],

[
    KC.TRNS,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,KC.F6,KC.F7,KC.F8,KC.F9,KC.F10,KC.F11,KC.F12,
    KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,
    KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.PGUP,KC.TRNS,
    KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.PGDN,KC.TRNS,
],
]

if __name__ == '__main__':
    keyboard.go()
