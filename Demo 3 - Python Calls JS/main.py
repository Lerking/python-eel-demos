import eel
from datetime import datetime as dt

eel.init("www")
eel.start("index.html", port = 8080, block=False)

while True:
    timestamp = dt.now()
    eel.addText("The time now is {}".format(timestamp.strftime("%I:%M:%S %p")))

    eel.sleep(1.0)