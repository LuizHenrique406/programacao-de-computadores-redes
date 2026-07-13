from machine import Pin
import neopixel
import time


while True:
    for pos in range(1):
        np = neopixel.NeoPixel(machine.Pin(7), 25)
        for led in range(25):
            sensor_temp = machine.ADC(4) 
            fator_conversao = 3.3 / 65535 
            valor_adc = sensor_temp.read_u16() * fator_conversao 
            temperatura = 27 - (valor_adc - 0.706) / 0.001721 
            print (temperatura)
            if temperatura > 40:
                np[pos] = (50, 0, 0)
                np[led] = (50, 0, 0)
                np.write()
                time.sleep(1)
            elif temperatura > 35 and temperatura < 40:
                np[pos] = (50, 20, 0)
                np[led] = (50, 20, 0)
                np.write()
                time.sleep(1)
            elif temperatura > 30 and temperatura < 35:
                np[pos] = (0, 0, 50)
                np[led] = (0, 0, 50)
                np.write()
                time.sleep(1)
            elif temperatura > 25 and temperatura < 30:
                np[pos] = (0, 50, 0)
                np[led] = (0, 50, 0)
                np.write()
                time.sleep(1)
            elif temperatura < 25 or temperatura == 25:
                np[pos] = (0, 0, 0)
                np[led] = (0, 0, 0)
                np.write()
                time.sleep(1)
