import RPi.GPIO as malinka

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
    while True:
        inputStr = input("Введите число от 0 до 255 / или нажмите 'q' чтобы выйти")

        if inputStr.isdigit():
            value = int(inputStr)
            if value >= levels:
                print("эээ. слишком много. давай по новой")
                continue
            signal = bin2dac(value)
            voltage = value / levels * maxVoltage
            print("Ввеленное число {:^3} -> {} в двоичной, напряжение на выходе = {:.4f}".format(value, signal, voltage))
        elif inputStr == 'q':
            break
        else:
            print("Число говорю напиши. Ци-фе-рку. Понятно?")
except KeyboardInterrupt:
    print("Программа прервана с клавиатуры")
else:
    print("Исключений нет")
finally:
    malinka.output(dac, malinka.LOW)
    malinka.cleanup(dac)
    print("очистка завершена")