from flask import Flask
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

song = {'Song': 'Somebody To Love', 'Author': 'Freddie Mercury', 'Group': 'Queen'}

@sock.route('/message')
def sendMsg(message):
    while True:
        id = message.receive()
        if id == 1:
            pass
        else:
            message.send(song['Song'])
            message.send(song['Author'])
            message.send(song['Group'])


