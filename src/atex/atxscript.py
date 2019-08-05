import serial
import time


class Sender:
    def sendsms(self, to, message):

        ser = serial.Serial('/dev/ttyACM0', 115200, timeout=5)
        time.sleep(1)
        ser.write(str.encode('ATZ\r'))
        time.sleep(1)
        ser.write(str.encode('AT+CMGF=1\r'))
        time.sleep(1)
        ser.write(str.encode('''AT+CMGS="''' + to + '''"\r'''))
        time.sleep(1)
        ser.write(str.encode(message + "\r"))
        time.sleep(1)
        ser.write(str.encode(chr(26)))
        time.sleep(1)
        ser.close()


# print("Filling and Sending msg")
# sendsms("0763722013", "test message send through python")
