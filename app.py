from flask import Flask, render_template, request, redirect
import xml.etree.ElementTree as ET


app = Flask(__name__)

songs = { }

i = 0

# song = {'Song': 'Somebody To Love', 'Author': 'Freddie Mercury', 'Group': 'Queen'}

# songs[0] = song

# print(songs)

def xml_injection(id, count):
    if id == 1:
        return render_template('index.html', songs = songs)
    else:
        while count < 10000:
            songs[count] = {'Song': 'Somebody To Love', 'Author': 'Freddie Mercury', 'Group': 'Queen'}
        return render_template('index.html', songs = songs)

@app.route('/', methods=['POST', 'GET'])
def index():
    global i
    if request.method == 'POST':
        song_name = request.form['song']
        song_author = request.form['author']
        song_group = request.form['group']
        try:
            songs[i] = {'Song': str(song_name), 'Author': str(song_author), 'Group': str(song_group)}
            i += 1
            print(songs)
            print(i)
            return redirect(('/'))
        except:
            return "There was an issue posting!"
    else:
        return xml_injection(1, 0)

@app.route('/delete/<int:id>')
def delete(id):
    try:
        songs[id] = { }
        print(songs)
        return redirect(('/'))
    except:
        return "There was an issue deleting!"

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    if request.method == 'POST':
        song_name = request.form['song']
        song_author = request.form['author']
        song_group = request.form['group']
        try:
            songs[id] = {'Song': str(song_name), 'Author': str(song_author), 'Group': str(song_group)}
            return redirect(('/'))
        except:
            return "There was an issue posting!"
    else:
        return render_template('update.html', songs = songs)

if __name__ == "__main__":
    app.run(debug=True)