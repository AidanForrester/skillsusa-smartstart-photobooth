import os
import subprocess
import digitalio
import board
import threading

from flask import Flask, send_from_directory

app = Flask(__name__)

rotbutton = digitalio.DigitalInOut(board.D26)
rotbutton.direction = digitalio.Direction.INPUT
rotbutton.pull = digitalio.Pull.UP

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/skills")
def download_photo():
    return send_from_directory(
        BASE_DIR,
        "skills.jpg",
        as_attachment=True
    )

def checkbutton():
	if rotbutton.value == False:
		subprocess.run(["python3", "photobooth.py"])

if __name__ == "__main__":
    def photosendtask():
        while True:
           checkbutton()
    photo_thread = threading.Thread(target=photosendtask)
    photo_thread.start()

app.run(host="0.0.0.0", port=8000)
