#Se importan bibliotecas necesarias
import time as T
#Parser de XML 
from xml.dom.minidom import parse
#Framework de Python para programación web
from flask import Flask, render_template, request

#Variables globales que se utilizan durante la ejecución del programa
app = Flask(__name__)
#El tiempo de ejecución de cada solicitud
time = 0
#Estructura de datos para guardar la información parseada del XML
songs = { }

#Función que recibe un nodo del XML parseado y construye el diccionario de esta forma
def getText(nodeList):
    songs = { }
    #Contador de espacios de etiquetas del XML
    i = 0
    #Ciclo que recorre el XML parseado y obtiene los nodos correspondientes para llenar el diccionario
    for node in nodeList:
        #El diccionario se llena de la forma: Título de la canción, Autor de la canción y Grupo al que pertenece
        songs[i] = {'Titulo': node.getElementsByTagName('Titulo')[0].firstChild.nodeValue, 'Autor': node.getElementsByTagName('Autor')[0].firstChild.nodeValue, 'Grupo': node.getElementsByTagName('Grupo')[0].firstChild.nodeValue,}
        i += 1
    return songs

#Se establece la ruta para que la aplicación web se comunique con el servidor, sus métodos son POST y GET
@app.route("/", methods=['GET', 'POST'])
#Función que parsea el XML enviado por el cliente mediante un POST e imprime sus datos en la paǵina
def parse_xml():
    #Variables globales importadas para su uso en la página web
    global songs, time
    #POST, envía el XML al servidor
    if request.method == 'POST':
        #Inicia a contar el tiempo
        start = T.time()
        #Obtiene el XML mediante el tag de 'files'
        xml = request.files['file']
        #Parsea el XML utilizando la biblioteca MiniDOM
        xml_data = parse(xml)
        #Obtiene todos los elementos dentro del tag 'CancionFavorita' y los guarda con una variable
        song = xml_data.getElementsByTagName('CancionFavorita')
        #Utiliza la función utilitaria para obtener el diccionario
        songs = getText(song)
        #Termina de contar el tiempo de ejecución
        end = T.time()
        #Obtiene la variable de tiempo de tiempo y la imprime en pantalla para interpretar resultados
        time = end - start
        print(time)
        #Retorna el HTML con las variables globales como variables internas para mostrarlos en pantalla
        return render_template('index.html', time = time, songs = songs)
    #GET, retorna los valores del XML y renderiza la página
    else:
        #Retorna el HTML con las variables globales como variables internas para mostrarlos en pantalla
        return render_template('index.html', time = time, songs = songs)

if __name__ == '__main__':
    print("Starting python app")
    #Inicia la aplicación web para su ejecución
    app.run(host='0.0.0.0', port=8080, debug=True)