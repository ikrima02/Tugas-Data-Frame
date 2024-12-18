import RPi.GPIO as GPIO
import time

BTN_1 = 4
BTN_2 = 17
leds = [5, 6, 12, 13, 16, 19]  # List tidak boleh diubah

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    # Setup pin button
    GPIO.setup(BTN_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(BTN_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    # Setup pin LED
    for led in leds:
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, GPIO.LOW)  # Memastikan LED mati saat awal

def fungsi1():
    # Menyalakan LED di pin 13, 6, dan 19
    target_leds = [13, 6, 19]
    for led in target_leds:
        GPIO.output(led, GPIO.HIGH)
    time.sleep(1)  # Durasi LED menyala, bisa disesuaikan
    for led in target_leds:
        GPIO.output(led, GPIO.LOW)

def main():
    setup()
    try:
        while True:
            # Logika jika BTN_1 ditekan
            if GPIO.input(BTN_1) == GPIO.HIGH:  # Tombol ditekan
                fungsi1()
                time.sleep(0.5)  # Debounce
    except KeyboardInterrupt:
        GPIO.cleanup()
main()
