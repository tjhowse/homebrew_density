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
    # 8ms is about 3m round trip. A 50ms timeout is reasonable.
    response_timeout_us = 50000
    START = 0
    END = 0
    # Send a 10us pulse on the trigger pin
    t.value(1)
    trigger_time = ticks_us()
    sleep_us(10)
    t.value(0)
    # Wait for the interrupts to set these globals.
    while START == 0 or END == 0:
        # Throw and exception if we get a timeout.
        if ticks_diff(ticks_us(), trigger_time) > response_timeout_us:
            raise ValueError("Timeout from ultrasonic")
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
    # Trigger pin
    t = Pin(13, Pin.OUT)
    # Input pin
    i = Pin(12, Pin.IN)
    i.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=callback)
    while True:
        try:
            print(get_avg_reading(t,i,avg_samples))
        except ValueError as e:
            print("Failed to get reading: {}".format(e))
        sleep_us(100000)

