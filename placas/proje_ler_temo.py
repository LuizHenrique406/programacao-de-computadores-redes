from machine import Pin
import neopixel
import time
sensor_temp = machine.ADC(4)
np = neopixel.NeoPixel(machine.Pin(7), 25)
joystick_x  = machine.ADC(27) 
joystick_y  = machine.ADC(26)
def temp():
    fator_conversao = 3.3 / 65535 
    valor_adc = sensor_temp.read_u16() * fator_conversao 
    temperatura = 27 - (valor_adc - 0.706) / 0.001721
    return temperatura
def atualiza_leds():
    num = []
    for i in range(1,25):
        num.append(i)
    num = num[::-1]
    for i in num:
        np[i] = np[i - 1]
def posi_x():
    posicao_x = joystick_x.read_u16()
    cofre = posicao_x
    posicao_x = joystick_x.read_u16()
    return cofre - posicao_x
leitura = 2
while True:
    temperatura = temp()
    if cofre - posicao_y > 2000:
        leitura = leitura - 0.1
    elif cofre - posicao_x < -2000:
        leitura = leitura + 0.1
    if leitura > 2:
        leitura = leitura - 0.1
    elif leitura < 0:
        leitura = leitura + 0.1
    if temperatura > 40 or temperatura == 40:
        np[0] = (50,0,0)
    elif temperatura > 35 and temperatura < 40:
        np[0] = (50,30,0)
    elif temperatura > 30 and temperatura < 35:
        np[0] = (0,0,50)
    elif temperatura > 25 and temperatura < 30:
        np[0] = (0,50,0)
    elif temperatura < 25:
        np[0] = (0,0,0)
    np.write()
    atualiza_leds()
    print(leitura)
    print(temperatura)
    time.sleep(leitura)
