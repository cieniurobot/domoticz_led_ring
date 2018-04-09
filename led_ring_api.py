from flask import Flask
from led_ring import LedRing
app = Flask(__name__)

@app.route("/on")
def on():
    led_ring = LedRing()
    led_ring.on()\

@app.route("/off")
def off():
    led_ring = LedRing()
    led_ring.off()

if __name__ == "__main__":
    app.run()