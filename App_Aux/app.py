from flask import Flask, render_template, request, redirect
import xml.etree.ElementTree as ET
import time as T

app = Flask(__name__)

tree = ET.parse('Queen.xml')
root = tree.getroot()
id = 0

def xml_injection(id, count, time):
    start = T.time()
    cancionFavorita = ET.Element('CancionFavorita')
    cancionFavorita.tail = "\n"
    cancionFavorita.text = "\n\t\t" 
    titulo = ET.SubElement(cancionFavorita, 'Titulo') 
    autor = ET.SubElement(cancionFavorita, 'Autor') 
    grupo = ET.SubElement(cancionFavorita, 'Grupo') 
    titulo.tail = "\n\t\t"
    autor.tail = "\n\t\t"
    grupo.tail = "\n\t\t"
    print("Va por acá")
    if id == "1":
        while count < 300:
            titulo.text = 'Bohemian Rhapsody'
            autor.text = 'Freddie Mercury'
            grupo.text = 'Queen' 
            cancionFavorita.append(titulo)
            cancionFavorita.append(autor)
            cancionFavorita.append(grupo)
            root[-1].tail = "\n\t"
            root.append(cancionFavorita)
            root.set('id', id)
            count += 1
            tree.write('Queen.xml')
        end = T.time()
        time = end - start
        print(time)
        return render_template('index.html', root = root, time = time)
    else:
        return render_template('index.html', root = root, time = time)

@app.route('/', methods=['POST', 'GET'])
def index():
    time = 0
    global id
    #POST
    if request.method == 'POST':
        start = T.time()
        cancionFavorita = ET.Element('CancionFavorita')
        cancionFavorita.tail = "\n"
        cancionFavorita.text = "\n\t\t" 
        titulo = ET.SubElement(cancionFavorita, 'Titulo') 
        autor = ET.SubElement(cancionFavorita, 'Autor') 
        grupo = ET.SubElement(cancionFavorita, 'Grupo') 
        titulo.tail = "\n\t\t"
        autor.tail = "\n\t\t"
        grupo.tail = "\n\t\t"
        try:
            titulo.text = request.form['song']
            autor.text = request.form['author']
            grupo.text = request.form['group']
            root[-1].tail = "\n\t"
            root.append(cancionFavorita)
            root.set('id', request.form['id'])
            tree.write('Queen.xml')
            id = request.form['id']
            end = T.time()
            time = end - start
            print(time)
            return redirect(('/'))
        except:
            end = T.time()
            time = end - start
            print(time)
            return "There was an issue posting!"
    #GET
    else:
        return xml_injection(id, 0, time)

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    time = 0
    if request.method == 'POST':
        start = T.time()
        cancionFavorita = ET.Element('CancionFavorita')
        cancionFavorita.tail = "\n"
        cancionFavorita.text = "\n\t\t" 
        titulo = ET.SubElement(cancionFavorita, 'Titulo') 
        autor = ET.SubElement(cancionFavorita,'Autor') 
        grupo = ET.SubElement(cancionFavorita, 'Grupo') 
        titulo.tail = "\n\t\t"
        autor.tail = "\n\t\t"
        grupo.tail = "\n\t\t"
        try:
            titulo.text = request.form['song']
            autor.text = request.form['author']
            grupo.text = request.form['group'] 
            root[-1].tail = "\n\t"
            root.insert(id, cancionFavorita)
            end = T.time()
            time = end - start
            print(time)
            return redirect(('/'))
        except:
            end = T.time()
            time = end - start
            print(time)
            return "There was an issue posting!"
    else:
        return xml_injection(id, 0, time)

if __name__ == "__main__":
    app.run(debug=True)