import RPi.GPIO as malinka
import time
dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3

def decimal2binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def bin2dac(value):
    signal = decimal2binary(value)
    malinka.output(dac, signal)
    return signal

malinka.setmode(malinka.BCM)
malinka.setup(dac, malinka.OUT, initial = malinka.LOW)

try:
    i = 0
    while i < 255:
        bin2dac(i)
        time.sleep(0.1)
        i += 1
    while i > 0:
        bin2dac(i)
        time.sleep(0.1)
        i -= 1
        continue
finally:
    malinka.output(dac, malinka.LOW)
    malinka.cleanup(dac)
    print("очистка завершена")
