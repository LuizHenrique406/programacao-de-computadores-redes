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
ref = [40,35,30,25]
soma = 1
leitura = 2
while True:
    temperatura = temp()
    posicao_y = joystick_y.read_u16()
    posicao_x = joystick_x.read_u16()
    if posicao_y > 32000:
        leitura -= 0.1
    else:
        leitura += 0. 
    if leitura > 2:
        leitura -= 0.1
    elif leitura < 0:
        leitura += 0.1
    if posicao_x > 35000:
        ref = list(map(lambda x:x - soma, ref))
        if ref[0] > 50:
            ref[0] -= 1
        if ref[1] > 40:
            ref[1] -= 1
        if ref[2] > 35:
            ref[2] -= 1
        if ref[3] > 30:
            ref[3] -= 1    
        print(ref)
    if posicao_x < 30000:
        ref = list(map(lambda x:x + soma, ref))
        if ref[0] < 25:
            ref[0] += 1
        if ref[1] <35:
            ref[1] += 1
        if ref[2] < 30:
            ref[2] += 1
        if ref[3] < 25:
            ref[3] += 1    
        print(ref) 
    if temperatura > ref[0] or temperatura == ref[0]:
        np[0] = (50,0,0)
    elif temperatura > ref[1] and temperatura < ref[0]:
        np[0] = (50,30,0)
    elif temperatura > ref[2] and temperatura < ref[1]:
        np[0] = (0,0,50)
    elif temperatura > ref[3] and temperatura < ref[2]:
        np[0] = (0,50,0)
    elif temperatura < ref[3]:
        np[0] = (0,0,0)
    np.write()
    atualiza_leds()
    print(temperatura)
    print(leitura)
    print(posicao_x)
    time.sleep(leitura)