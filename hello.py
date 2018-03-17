import bme280
import flask
import smbus2

port = 1
address = 0x76
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus, address)

app = flask.Flask(__name__)

@app.route('/')
def index():
    return "Hello, World"

@app.route('/temperature')
def temperature():
    data = bme280.sample(bus, address)
    return "{}".format(data.temperature)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
