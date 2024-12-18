import RPi.GPIO as GPIO
import time

# Konfigurasi pin GPIO untuk tombol dan LED
buttons = [4, 12, 17]  # Tombol 1, Tombol 2, Tombol 3
led_pins = [18, 5, 6]  # LED 1, LED 2, LED 3

def setup_gpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    for pin in led_pins:
        GPIO.setup(pin, GPIO.OUT)
    for button in buttons:
        GPIO.setup(button, GPIO.IN)

def turn_on_leds_sequentially(pins, delay=0.4):
    """Menyalakan LED secara berurutan sesuai daftar pins."""
    for pin in pins:
        GPIO.output(pin, True)
        time.sleep(delay)
        GPIO.output(pin, False)

def main():
    setup_gpio()
    
    while True:
        if GPIO.input(buttons[0]) == 1 and GPIO.input(buttons[1]) == 0 and GPIO.input(buttons[2]) == 0:
            # Tombol 1: Lampu menyala searah LED -> LED2 -> LED3
            turn_on_leds_sequentially(led_pins)
        elif GPIO.input(buttons[1]) == 1 and GPIO.input(buttons[0]) == 0 and GPIO.input(buttons[2]) == 0:
            # Tombol 2: Lampu menyala mundur LED3 -> LED2 -> LED
            turn_on_leds_sequentially(reversed(led_pins))
        elif GPIO.input(buttons[2]) == 1:
            # Tombol 3: Lampu menyala searah LED -> LED2 -> LED3
            turn_on_leds_sequentially(led_pins)
        else:
            # Jika tidak ada tombol ditekan, semua LED mati
            for pin in led_pins:
                GPIO.output(pin, False)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
