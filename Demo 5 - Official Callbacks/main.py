import eel

eel.init("www")
eel.start("index.html", port = 8080, block=False)

@eel.expose
def send(msg):
    print("Received Message: " + msg)
    return "ok"

while True:
    text = eel.readTextBox()()
    print("Text box contents: {}".format(text))
    eel.sleep(2.0)