from flask import Flask,render_template
import requests
from dotenv import load_dotenv,dotenv_values
app=Flask(__name__)

config = dotenv_values('.env')

app = Flask (__name__)
def get_weather_data (city):
    API_KEY = config['API_KEY']
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang&appid={API_KEY}'
    r = requests.get(url).json()
    print(r)
    return r

@app.route('/prueba')
def prueba():
    clima=get_weather_data('london')
    temperatura=str(clima['main']['temp'])
    descripcion= str(clima['weather'][0]['description'])
    icono=str(clima['weather'][0]['icon'])
    r_json={
        'ciudad': 'london',
        'temperatura':temperatura,
        'descripcion': descripcion,
        'icono': icono
        }
    return render_template('weather.html', clima = r_json)
   



@app.route('/about')
def hello_CV():
    return render_template('CV.html')


if __name__ == '__main__':
    app.run(debug = True)

@app.route('/clima')
def clima_page():
    return render_template('resultado.json')

@app.route('/clima')
def clima():
    return 'CLIMA'

if __name__ == '__main__':
    app.run(debug = True)






































































































































































































































