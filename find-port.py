import serial.tools.list_ports


def find_arduino_port():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        print(f"port: {p.description}")
        if 'Arduino' in p.description:
            return p.device
    return None


arduino_port = find_arduino_port()

if arduino_port is not None:
    print(f"arduino_port: {arduino_port}")
else:
    print("Could not find an Arduino device.")
