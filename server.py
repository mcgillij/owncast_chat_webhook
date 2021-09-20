from flask import Flask, request, abort
# from pprint import pprint

app = Flask(__name__)

file_to_write_to = '/home/j/obs_stuffs/chatlog.txt'

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        # pprint(request.json)
        message = request.json.get('eventData').get('body')
        user = request.json.get('eventData').get('user').get('displayName')

        if user and message:
            write_out_chatlog(user, message)
        return 'success', 200
    else:
        abort(400)

def write_out_chatlog(user, message):
    with open(file_to_write_to, mode='a') as chatlog:
        chatlog.write(f"{user}: {message}\n")



if __name__ == "__main__":
    app.run(host='0.0.0.0')

