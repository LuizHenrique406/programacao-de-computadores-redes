from machine import Pin
import time

def obtem_temperatura():
    fator_convesao = 3.3 / 65535
    valor_adc = sensor_temp.read_u16() * fator_convesao
    temperatura = 27 - (valor_adc - 0.706) / 0.001721
    return temperatura
sensor_temp = machine.ADC(4)

verde = Pin(11, Pin.OUT)
azul = Pin(12, Pin.OUT)
vermelho = Pin(13, Pin.OUT)

while True:
    temperatura = obtem_temperatura()
    if temperatura < 30:
        verde.value(True)
        time.sleep(1)
        verde.value(False)
        time.sleep(1)
    if 30 < temperatura < 32:
        azul.value(True)
        time.sleep(1)
        azul.value(False)
        time.sleep(1)
    if temperatura > 32:
        vermelho.value(True)
        time.sleep(1)
        vermelho.value(False)
        time.sleep(1)
