from machine import Pin,freq
from utime import sleep_us, ticks_us, ticks_cpu,ticks_diff

START = 0
END = 0

def callback(p):
    global START,END,ticks_cpu
    if START == 0:
        START = ticks_cpu()
    else:
        END = ticks_cpu()

def get_reading(t,i):
    global START,END
    START = 0
    END = 0
    t.value(1)
    sleep_us(10)
    t.value(0)
    while START == 0 or END == 0:
        sleep_us(10)
    return ticks_diff(END,START)

def get_avg_reading(t,i,n):
    avg = 0
    for _ in range(n):
        avg += get_reading(t,i)
        sleep_us(1000)
    return int(avg / n)

def go():
    avg_samples = 10;

    freq(160000000);
    t = Pin(13, Pin.OUT)
    i = Pin(12, Pin.IN)
    i.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=callback)
    while True:
        print(get_avg_reading(t,i,avg_samples))
        sleep_us(100000)

