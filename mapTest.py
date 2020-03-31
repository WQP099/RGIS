import folium
import webbrowser
import os

map = folium.Map(
            location=[39.90,116.40],
            zoom_start=15,
            height=400,
            width=800,
            tiles='http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=7&x={x}&y={y}&z={z}',
            attr="高德地图"
        )
#print("debug",mapjson)
map.save('schools_map.html')
htmlf=open('schools_map.html','r',encoding="utf-8")
htmlcont=htmlf.read()
htmlcont = htmlcont.replace("https://cdn.jsdelivr.net/npm/leaflet@1.5.1/dist/leaflet.js","js/leaflet.js")
htmlcont = htmlcont.replace('https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js','js/bootstrap.min.js')
htmlcont = htmlcont.replace('https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js','js/leaflet.awesome-markers.js')
htmlcont = htmlcont.replace('https://cdn.jsdelivr.net/npm/leaflet@1.5.1/dist/leaflet.css','css/leaflet.css')
htmlcont = htmlcont.replace('https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css','css')
htmlcont = htmlcont.replace('https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css','css/font-awesome.min.css')
htmlcont = htmlcont.replace('https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css','css/leaflet.awesome-markers.css')
htmlcont = htmlcont.replace('https://rawcdn.githack.com/python-visualization/folium/master/folium/templates/leaflet.awesome.rotate.css','css/leaflet.awesome.rotate.css')
print("debug", htmlcont)
new_html = open('schools_map.html','w')
new_html.write(htmlcont)
new_html.close()
htmlf.close()
# current_work_dir = os.path.dirname(__file__)
# file_path = current_work_dir+'/schools_map.html'
# print("filePath", file_path)
# file_url = QUrl(os.path.abspath("./schools_map.html"))
# print("fileURL " , file_url)
# webbrowser.open('schools_map.html')
# view = QWebEngineView()
# view.load(QUrl("http://www.baidu.com/"))
# view.show()
#display(map)

