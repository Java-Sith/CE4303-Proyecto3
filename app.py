from flask import Flask, render_template, request, redirect
import xml.etree.ElementTree as ET
import time as T

app = Flask(__name__)

tree = ET.parse('Queen.xml')
root = tree.getroot()

def xml_injection(id, count):
    start = T.time()
    cancionFavorita = ET.Element('CancionFavorita')
    titulo = ET.Element('Titulo') 
    autor = ET.Element('Autor') 
    grupo = ET.Element('Grupo') 
    if id == 1:
        while count < 100000:
            titulo.text = 'Bohemian Rhapsody'
            autor.text = 'Freddie Mercury'
            grupo.text = 'Queen'
            titulo.tail = "\n    "
            autor.tail = "\n    "
            grupo.tail = "\n    "
            cancionFavorita.append(titulo)
            cancionFavorita.append(autor)
            cancionFavorita.append(grupo)
            cancionFavorita.tail = "\n    "
            root.append(cancionFavorita)
            root.set('id', 1)
            count += 1
            tree.write('Queen.xml')
        end = T.time()
        print(end - start)
        return render_template('index.html', root = root)
    else:
        return render_template('index.html', root = root)

@app.route('/', methods=['POST', 'GET'])
def index():
    #POST
    if request.method == 'POST':
        start = T.time()
        cancionFavorita = ET.Element('CancionFavorita')
        titulo = ET.Element('Titulo') 
        autor = ET.Element('Autor') 
        grupo = ET.Element('Grupo') 
        try:
            titulo.text = request.form['song']
            autor.text = request.form['author']
            grupo.text = request.form['group']
            titulo.tail = "\n    "
            autor.tail = "\n    "
            grupo.tail = "\n    "
            cancionFavorita.append(titulo)
            cancionFavorita.append(autor)
            cancionFavorita.append(grupo)
            cancionFavorita.tail = "\n    "
            root.append(cancionFavorita)
            root.set('id', request.form['id'])
            tree.write('Queen.xml')
            end = T.time()
            print(end - start)
            return redirect(('/'))
        except:
            end = T.time()
            print(end - start)
            return "There was an issue posting!"
    #GET
    else:
        return xml_injection(request.form['id'], 0)

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    if request.method == 'POST':
        start = T.time()
        cancionFavorita = ET.Element('CancionFavorita')
        titulo = ET.Element('Titulo') 
        autor = ET.Element('Autor') 
        grupo = ET.Element('Grupo') 
        cancionFavorita = ET.Element('CancionFavorita')
        titulo = ET.Element('Titulo') 
        autor = ET.Element('Autor') 
        grupo = ET.Element('Grupo') 
        try:
            titulo.text = request.form['song']
            autor.text = request.form['author']
            grupo.text = request.form['group']
            titulo.tail = "\n    "
            autor.tail = "\n    "
            grupo.tail = "\n    "
            cancionFavorita.insert(0, titulo)
            cancionFavorita.insert(1, autor)
            cancionFavorita.insert(2, grupo)
            cancionFavorita.tail = "\n    "
            root.insert(id, cancionFavorita)
            end = T.time()
            print(end - start)
            return redirect(('/'))
        except:
            end = T.time()
            print(end - start)
            return "There was an issue posting!"
    else:
        return xml_injection(0, 0)

if __name__ == "__main__":
    app.run(debug=True)