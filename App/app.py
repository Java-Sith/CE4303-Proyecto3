import time as T
from lxml import etree as ET
from xml.dom.minidom import parse
import xmltodict as X
from flask import Flask, render_template, request

app = Flask(__name__)
time = 0
songs = { }

def getText(nodeList):
    songs = { }
    i = 0
    for node in nodeList:
        songs[i] = {'Titulo': node.getElementsByTagName('Titulo')[0].firstChild.nodeValue, 'Autor': node.getElementsByTagName('Autor')[0].firstChild.nodeValue, 'Grupo': node.getElementsByTagName('Grupo')[0].firstChild.nodeValue,}
        i += 1
    return songs

@app.route("/", methods=['GET', 'POST'])
def parse_xml():
    global songs, time
    if request.method == 'POST':
        start = T.time()
        xml = request.files['file']
        xml_data = parse(xml)
        #buffer = io.BytesIO()
        #parser = ET.XMLParser(dtd_validation=True)
        #xml_data = ET.parse(xml, parser=parser)
        song = xml_data.getElementsByTagName('CancionFavorita')
        songs = getText(song)
        end = T.time()
        time = end - start
        print(time)
        return render_template('index.html', time = time, songs = songs)
        #return xml_data.version
    else:
        return render_template('index.html', time = time, songs = songs)

if __name__ == '__main__':
    print("Starting python app")
    # xml_data = parse('Queen.xml')
    # song = xml_data.getElementsByTagName('CancionFavorita')
    # songs = getText(song)
    # print(songs)
    # for key, song in songs.items():
    #     print(song['Titulo'])
    #     print(song['Autor'])
    #     print(song['Grupo'])
    app.run(host='0.0.0.0', port=8080, debug=True)