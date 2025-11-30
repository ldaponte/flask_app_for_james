from flask import Flask, request
import serial
import time

app = Flask(__name__)

def read_serial_to_file(port='/dev/ttyUSB0', baudrate=9600, output_file='serial_data.txt'):
    """Read a line of data from serial port and write it to a file"""
    try:
        ser = serial.Serial(port, baudrate=baudrate, timeout=1)
        print(f"Connected to {port} at {baudrate} baud")

        with open(output_file, 'a') as f:
            data = ser.readline()
            decoded_data = data.decode('utf-8').strip()
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            log_entry = f"[{timestamp}] {decoded_data}\n"
            f.write(log_entry)
            print(f"Received: {decoded_data}")

        ser.close()

    except Exception as e:
        print(f"Error: {e}")

@app.route('/hello/<name>')
def hello_name(name):
    """Route that takes a name parameter in the URL path"""
    timestamp = time.strftime('%Y%m%d_%H%M%S')
    filename = f"serial_data_{timestamp}.txt"
    read_serial_to_file(output_file=filename)
    return f"hello {name}"

@app.route('/hello')
def hello_query():
    """Route that takes a name parameter as a query string"""
    name = request.args.get('name', 'world')
    return f"hello {name}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
