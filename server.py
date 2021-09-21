from datetime import datetime
from dateutil import parser
from flask import Flask, request, abort

app = Flask(__name__)

file_to_write_to = '/home/j/obs_stuffs/chatlog.txt'

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        message = request.json.get('eventData').get('body')
        user = request.json.get('eventData').get('user').get('displayName')
        timestamp = request.json.get('eventData').get('timestamp')
        formatted = datetime.strftime(parser.isoparse(timestamp), '%H:%M:%S')

        if user and message and timestamp:
            write_out_chatlog(formatted, user, message)
        return 'success', 200
    else:
        abort(400)

def write_out_chatlog(timestamp, user, message):
    with open(file_to_write_to, mode='a') as chatlog:
        chatlog.write(f"{timestamp} {user}: {message}\n")



if __name__ == "__main__":
    app.run(host='0.0.0.0')
