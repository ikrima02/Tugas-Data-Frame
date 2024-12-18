import RPi.GPIO as GPIO
import time

button = 4
button1 = 12
button2 = 17  # Tambahkan tombol baru
led = 18
led2 = 5
led3 = 6

def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)
    GPIO.setup(led2, GPIO.OUT)
    GPIO.setup(led3, GPIO.OUT)
    GPIO.setup(button, GPIO.IN)
    GPIO.setup(button1, GPIO.IN)
    GPIO.setup(button2, GPIO.IN)  # Konfigurasi tombol baru
    
    while True:
        if GPIO.input(button) == 1 and GPIO.input(button1) == 0 and GPIO.input(button2) == 0:
            # Lampu berkedip secara berurutan: LED -> LED2 -> LED3
            GPIO.output(led, True)
            time.sleep(0.4)
            GPIO.output(led, False)
            GPIO.output(led2, True)
            time.sleep(0.4)
            GPIO.output(led2, False)
            GPIO.output(led3, True)
            time.sleep(0.4)
            GPIO.output(led3, False)
        elif GPIO.input(button1) == 1 and GPIO.input(button) == 0 and GPIO.input(button2) == 0:
            # Lampu berkedip secara berurutan mundur: LED3 -> LED2 -> LED
            GPIO.output(led3, True)
            time.sleep(0.4)
            GPIO.output(led3, False)
            GPIO.output(led2, True)
            time.sleep(0.4)
            GPIO.output(led2, False)
            GPIO.output(led, True)
            time.sleep(0.4)
            GPIO.output(led, False)
        elif GPIO.input(button2) == 1:  # Logika untuk tombol baru
            # Lampu menyala searah jarum jam: LED -> LED2 -> LED3
            GPIO.output(led, True)
            time.sleep(0.4)
            GPIO.output(led, False)
            GPIO.output(led2, True)
            time.sleep(0.4)
            GPIO.output(led2, False)
            GPIO.output(led3, True)
            time.sleep(0.4)
            GPIO.output(led3, False)
        else:
            # Semua lampu mati
            GPIO.output(led, False)
            GPIO.output(led2, False)
            GPIO.output(led3, False)
            
if _name_ == '_main_':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()