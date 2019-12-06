from flask import Flask
import folium
app = Flask(__name__)

Songkhla_detail = '''
    Songkhla, also known as Singgora or Singora, is a city in Songkhla Province of southern Thailand, 
    near the border with Malaysia. As of 2006 it had a population of 75,048. Songkhla lies 968 km south of Bangkok
    '''
Hatyai_detail = '''
Hat Yai, a city in Thailand's far south near the Malaysian border, is a sprawling commercial hub and shopping destination. 
At the Khlong Hae Floating Market, vendors sell local foods and handicrafts from traditional boats docked in a canal. 
The Wat Hat Yai Nai temple is known for its 35m-long reclining Buddha. Outside the city center, 
Hat Yai Park is a hilly green area with a standing Buddha statue and a cable car.
'''
Satun_detail = '''
Satun is one of the southern provinces of Thailand. 
Neighboring provinces are Trang, Phatthalung, and Songkhla. To the south it borders Perlis of Malaysia
'''
Provinces = [dict(
                  name="Songkhla",
                  coords=[7.1898,100.5954],
                  detail=Songkhla_detail),
             dict(
                  name="Hatyai",
                  coords=[7.008661,100.474687],
                  detail=Hatyai_detail),
            dict(
                  name="Satun",
                  coords=[6.623918, 100.067206],
                  detail=Satun_detail) ]
@app.route('/')
def home():
    return '<h1><a href="/map">Map</a></h1>'

@app.route('/map')
def map():
    start_coords = (7.1898, 100.5954) # ละติจูด,ลองจิจูด ของสงขลา
    folium_map = folium.Map(location=start_coords,
                             zoom_start=14)
    Markers = folium.FeatureGroup(name="Markers")
    for p in Provinces:
        Markers.add_child(folium.Marker(location=p['coords'],
                                        popup=folium.Popup(p['detail'],
                                                           max_width=400,min_width=300),
                                        tooltip=f"<b> {p['name']} </b>"))
    
    folium_map.add_child(Markers)
    return folium_map._repr_html_() # แสดงออกมาเป็น html

if __name__ == '__main__':
    app.run(debug=True)
