import RPi.GPIO as malinka
malinka.setmode(malinka.BCM)
malinka.setup(27, malinka.OUT)
def ChangeDutyCycle(value):
    p = malinka.PWM(27, 1000)
    p.start(value)
    input('Press return to stop:') 
    p.stop()
    malinka.cleanup()
try:
    while True:
        inputStr = input("Введите число от 0 до 100 / или нажмите 'q' чтобы выйти")

        if inputStr.isdigit():
            value = int(inputStr)
            if value >= 100:
                print("эээ. слишком много. давай по новой")
                
            ChangeDutyCycle(value)
            continue
        elif inputStr == 'q':
            break
        else:
            print("Число говорю напиши. Ци-фе-рку. Понятно?")
except KeyboardInterrupt:
    print("Программа прервана с клавиатуры")
else:
    print("Исключений нет")
    
finally:
    malinka.cleanup(27)
    print("очистка завершена")