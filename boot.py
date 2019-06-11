import network,time
import secrets
ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    time.sleep(1)
    sta_if.connect(secrets.wifi_ssid, secrets.wifi_psk)
    attempts = 0
    while not sta_if.isconnected():
        time.sleep(1)
        attempts += 1
        if attempts > 5:
            print("I give up connecting to wifi")
            import machine
            machine.reset()
print('network config:', sta_if.ifconfig())
time.sleep(2)
import ping
while (True):
    try:
        ping.go()
    except Exception as e :
        print("Caught exception in main, rebooting: {}".format(e))
        time.sleep(5)
        import machine
        machine.reset()
