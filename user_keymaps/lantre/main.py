import supervisor

from kb import KMKKeyboard

from kmk.extensions.peg_oled_Display import (
    Oled,
    OledData,
    OledDisplayMode,
    OledReactionType,
)
from kmk.extensions.peg_rgb_matrix import Rgb_matrix
from kmk.handlers.sequences import ENTER_KEY, send_string
from kmk.hid import HIDModes
from kmk.keys import KC
from kmk.modules.holdtap import HoldTap, HoldTapRepeat
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.capsword import CapsWord

keyboard = KMKKeyboard()
holdtap = HoldTap()
layers = Layers()
caps_word = CapsWord()

keyboard.modules.append(layers)
keyboard.modules.append(holdtap)
keyboard.modules.append(caps_word)

oled = Oled(
    OledData(
        corner_one={0: OledReactionType.STATIC, 1: ['qwertyzzzz']},
        corner_two={
            0: OledReactionType.LAYER,
            1: ['1', '2', '3', '4', '5', '6', '7', '8'],
        },
        corner_three={
            0: OledReactionType.LAYER,
            1: ['base', 'raise', 'lower', 'adjust', '5', '6', '7', '8'],
        },
        corner_four={
            0: OledReactionType.LAYER,
            1: ['qwertyzzz', 'nums', 'shifted', 'leds', '5', '6', '7', '8'],
        },
    ),
    toDisplay=OledDisplayMode.TXT,
    flip=False,
)
keyboard.extensions.append(oled)

# Default RGB matrix colours
rgb = Rgb_matrix(
    ledDisplay=[
        [85, 0, 255],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [85, 0, 255],
        [85, 0, 255],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [85, 0, 255],
        [85, 0, 255],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [85, 0, 255],
        [85, 0, 255],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [85, 0, 255],
        [85, 0, 255],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [85, 0, 255],
        [85, 0, 255],
        [85, 0, 255],
        [85, 0, 255],
        [0, 255, 234],
        [0, 255, 234],
        [85, 0, 255],
        [85, 0, 255],
        [85, 0, 255],
        [85, 0, 255],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [85, 0, 255],
        [85, 0, 255],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [0, 255, 234],
        [85, 0, 255],
    ],
    split=True,
    rightSide=False,
    disable_auto_write=True,
)
keyboard.extensions.append(rgb)

split = Split(data_pin=keyboard.rx, data_pin2=keyboard.tx, uart_flip=False)
keyboard.modules.append(split)

# Combos
from kmk.modules.combos import Combos, Chord, Sequence
combos = Combos()
keyboard.modules.append(combos)

combos.combos = [
    Chord((KC.D, KC.F), KC.ESC),
    Chord((KC.J, KC.K), KC.TAB)
]

# Hold Tap
ENTSFT = KC.HT(KC.ENT, KC.LSFT)
ESCTL = KC.HT(KC.ESC, KC.LCTL)
TABMO1 = KC.HT(KC.TAB, KC.MO(1))
BSPMO2 = KC.HT(KC.BSPC, KC.MO(2), repeat=HoldTapRepeat.TAP)
CAPSGUI = KC.HT(KC.CW, KC.LGUI)

# Keymap
keyboard.keymap = [
    [ # Layer 0
        KC.GRV,  KC.N1,   KC.N2,   KC.N3,    KC.N4,   KC.N5,                      KC.N6,   KC.N7,    KC.N8,    KC.N9,  KC.N0,    KC.GRV,
        KC.TAB,  KC.Q,    KC.W,    KC.E,     KC.R,    KC.T,                       KC.Y,    KC.U,     KC.I,     KC.O,   KC.P,     KC.MINS,
        ESCTL,   KC.A,    KC.S,    KC.D,     KC.F,    KC.G,                       KC.H,    KC.J,     KC.K,     KC.L,   KC.SCLN,  KC.QUOT,
        CAPSGUI, KC.Z,    KC.X,    KC.C,     KC.V,    KC.B,   KC.LBRC, KC.RBRC,   KC.N,    KC.M,     KC.COMMA, KC.DOT, KC.SLSH,  KC.RSFT,
                                   KC.LGUI,  KC.LALT, TABMO1, ENTSFT,  KC.SPC,    BSPMO2, KC.DEL, KC.RGUI,
        # Encoders
        KC.AUDIO_VOL_UP,
        KC.AUDIO_VOL_DOWN,
        KC.MEDIA_PREV_TRACK,
        KC.MEDIA_NEXT_TRACK,
    ],
    [ # Layer 1 - Symbols
        KC.F11,  KC.F1,     KC.F2,   KC.F3,   KC.F4,   KC.F5,                     KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10, KC.F12,
        KC.TRNS, KC.QUOTE,  KC.DQT,  KC.CIRC, KC.QUES, KC.GRV,                    KC.LBRC, KC.LABK, KC.EQL,  KC.RABK, KC.RBRC, KC.TRNS,
        KC.TRNS, KC.EXLM,   KC.AT,   KC.HASH, KC.DLR,  KC.PERC,                   KC.LCBR, KC.LPRN, KC.COLN, KC.RPRN, KC.RCBR, KC.TRNS,
        KC.TRNS, KC.BSLASH, KC.TILD, KC.PIPE, KC.AMPR, KC.SCLN, KC.TRNS, KC.TRNS, KC.SLSH, KC.ASTR, KC.MINS, KC.PLUS, KC.UNDS, KC.TRNS,
                                     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.DEL,  KC.TRNS,
        # Encoders
        KC.AUDIO_VOL_UP,
        KC.AUDIO_VOL_DOWN,
        KC.MEDIA_PREV_TRACK,
        KC.MEDIA_NEXT_TRACK,
    ],
    [ # Layer 2 - Nav/Num
        KC.N2,   KC.EXLM, KC.AT,   KC.HASH, KC.DLR,  KC.PERC,                   KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN,  KC.RPRN, KC.TILD,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,                   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  KC.PLUS, KC.UNDS,
        KC.TRNS, KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                     KC.LEFT, KC.DOWN, KC.UP,   KC.RIGHT, KC.COLN, KC.DQT,
        KC.TRNS, KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.LCBR, KC.RCBR, KC.TRNS, KC.TRNS, KC.LABK, KC.RABK,  KC.QUES, KC.TRNS,
                                   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.AUDIO_VOL_UP,
        KC.AUDIO_VOL_DOWN,
        KC.MEDIA_PREV_TRACK,
        KC.MEDIA_NEXT_TRACK,
    ],
    [
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,                   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,                   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,                   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
                                   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        # Encoders
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
    ],
    [
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,                   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,                   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,                   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
                                   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        # Encoders
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
    ],
    [
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,                   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,                   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,                   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
                                   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        # Encoders
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
    ],
    [
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,                   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,                   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,                   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
                                   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        # Encoders
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
    ],
    [
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,                   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,                   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,                   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
                                   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        # Encoders
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
        KC.TRNS,
    ],
]
if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.USB)
