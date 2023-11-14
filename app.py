from flask import Flask, render_template
import requests
from dotenv import load_dotenv,dotenv_values

app = Flask(__name__)

config = dotenv_values ('.env')

def get_weather_data(city):
    API_KEY = config['API_KEY']
    url=f'https://api.openweathermap.org/data/2.5/weather?q={ city }&appid={API_KEY}&units=metric&lang=es'
    r = requests.get(url).json()
    return r 

@app.route('/prueba')
def prueba():
    clima = get_weather_data('Ambato')
    temperatura = str(clima['main']['temp'])
    descripcion= str(clima['weather'][0]['description'])
    icono= str(clima['weather'][0]['icon'])

    r_json= {
            'ciudad':'Ambato',
            'temperatura': temperatura,
             'descripcion':descripcion,
             'icono':icono
             }  
    return render_template('weather.html',clima=r_json)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/clima')
def clima():
    return 'obtener todo la informacion del clima'

if __name__ == '_main_':
    app.run(debug=True)










































































