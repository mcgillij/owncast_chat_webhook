import os
from datetime import datetime
from dateutil import parser
from flask import Flask, request, abort

app = Flask(__name__)

FILE_TO_WRITE_TO = '/home/j/obs_stuffs/chatlog.txt'

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        message = request.json['eventData'].get('body')
        user = request.json['eventData'].get('user').get('displayName')
        timestamp = request.json['eventData'].get('timestamp')
        formatted = datetime.strftime(parser.isoparse(timestamp), '%H:%M:%S')

        if user and message and timestamp:
            write_out_chatlog(formatted, user, message)
        return 'success', 200
    else:
        abort(400)


def check_for_tts(message):
    if message.startswith("TTS:"):
        speak = message.split('TTS:')[1]
        os.system(f'echo "{speak}" | festival --tts')


def write_out_chatlog(timestamp, user, message):
    with open(FILE_TO_WRITE_TO, mode='a') as chatlog:
        chatlog.write(f"{timestamp} {user}: {message}\n")
        check_for_tts(message)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
