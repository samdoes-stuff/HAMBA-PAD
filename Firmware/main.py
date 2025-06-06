from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
import busio
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.extensions.display import Display, SSD1306
import board
from kmk.macros import simple_key_sequence

keyboard = KMKKeyboard()

# --- Hardware Configuration ---
keyboard.row_pins = ()
keyboard.col_pins = (
    board.GP3,  # SW1
    board.GP4,  # SW2
    board.GP2,  # SW3
    board.GP1,  # SW4
    board.GP0,  # SW5
    board.GP28, # SW6
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# --- Brute-Force App Launch Macros ---
def open_deepseek():
    return simple_key_sequence([
        # Triple-tap Win key to ensure Start Menu opens
        KC.LGUI, KC.MACRO_SLEEP_MS(300),
        KC.LGUI, KC.MACRO_SLEEP_MS(300),
        KC.LGUI, KC.MACRO_SLEEP_MS(500),
        
        # Type app name with error correction
        KC.STRING("deep"), KC.MACRO_SLEEP_MS(100),
        KC.BSPC, KC.MACRO_SLEEP_MS(100),
        KC.STRING("DeepSeek"), KC.MACRO_SLEEP_MS(500),
        KC.ENTER
    ])

def open_gmail():
    return simple_key_sequence([
        # Open Run dialog with Win+R
        KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(800),
        
        # Type URL with clear previous content
        KC.STRING("        "), KC.MACRO_SLEEP_MS(100),  # Clear field
        KC.BSPC, KC.MACRO_SLEEP_MS(100),
        KC.STRING("https://gmail.com"), KC.MACRO_SLEEP_MS(300),
        KC.ENTER
    ])

def open_slack():
    return simple_key_sequence([
        # Ensure Start Menu opens
        KC.LGUI, KC.MACRO_SLEEP_MS(500),
        
        # Type with error correction
        KC.STRING("sl"), KC.MACRO_SLEEP_MS(100),
        KC.BSPC, KC.MACRO_SLEEP_MS(100),
        KC.STRING("Slack"), KC.MACRO_SLEEP_MS(500),
        KC.ENTER
    ])

def open_fusion360():
    return simple_key_sequence([
        KC.LGUI, KC.MACRO_SLEEP_MS(500),
        KC.STRING("fu"), KC.MACRO_SLEEP_MS(100),
        KC.BSPC, KC.MACRO_SLEEP_MS(100),
        KC.STRING("Fusion 360"), KC.MACRO_SLEEP_MS(500),
        KC.ENTER
    ])

def open_youtube():
    return simple_key_sequence([
        KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(800),
        KC.STRING("        "), KC.MACRO_SLEEP_MS(100),
        KC.BSPC, KC.MACRO_SLEEP_MS(100),
        KC.STRING("https://youtube.com"), KC.MACRO_SLEEP_MS(300),
        KC.ENTER
    ])

# NEW FUNCTION FOR EASYEDA
def open_easyeda():
    return simple_key_sequence([
        KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(800),
        KC.STRING("        "), KC.MACRO_SLEEP_MS(100),
        KC.BSPC, KC.MACRO_SLEEP_MS(100),
        KC.STRING("https://easyeda.com"), KC.MACRO_SLEEP_MS(300),
        KC.ENTER
    ])

# --- Keymap ---
keyboard.keymap = [
    [
        open_deepseek(),    # SW1 - DeepSeek
        open_gmail(),       # SW2 - Gmail
        open_slack(),       # SW3 - Slack
        open_fusion360(),   # SW4 - Fusion 360
        open_youtube(),     # SW5 - YouTube
        open_easyeda()      # SW6 - EasyEDA (REPLACED MEDIA KEY)
    ]
]

# --- Display Setup ---
i2c_bus = busio.I2C(board.GP7, board.GP6)
driver = SSD1306(i2c=i2c_bus, device_address=0x3C)
display = Display(
    display=driver,
    width=128,
    height=32,
    flip=False,
    brightness=0.8,
    dim_time=20,
    off_time=60,
)
keyboard.extensions.append(display)

# --- Encoder Setup ---
encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.GP26, board.GP27, board.GP29),)  # Rotary A, B, Switch
encoder_handler.map = [((KC.VOLD, KC.VOLU),)]  # Volume control
keyboard.modules.append(encoder_handler)

# --- Start Keyboard ---
if __name__ == '__main__':
    keyboard.go()
