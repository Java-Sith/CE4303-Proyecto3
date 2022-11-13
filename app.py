from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

""" songs = {{}}

song = {'Song': 'Somebody To Love', 'Author': 'Freddie Mercury', 'Group': 'Queen'}

songs[0] = song

i = 0  """

songs = []

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        song_content = request.form['content']
        try:
            songs.append(song_content)
            print(songs)
            return redirect('/')
        except:
            return "There was an issue posting!" + str(song_content)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)