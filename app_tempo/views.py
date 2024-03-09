from django.shortcuts import render
import json
import urllib.request

# Create your views here.

def index(request):
    if request.method == 'POST':                                                                                  # method do fomulário html
        cidade = request.POST['cidade']         
        resultado = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid=a8a48f552f089c60b8734a17d7305a0b&units=metric').read() #&units=metric muda pra C
        json_data = json.loads(resultado)                                                                         # organiza o .json
        data = {                                                                                                  # transformando o json para DICIONARIO - usado em sala de aula
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp'])+' C° ',
            "feels_like": str(json_data['main']['feels_like']) + ' C° ',
            "humidity": str(json_data['main']['humidity']) + '%',
            "pressure": str(json_data['main']['pressure']) + 'hPa',
        }

    else:                                                   # ELSE PRA NAO DAR ERRO, pq ele pensa que não foi declarado (?)
        cidade = ''
        data = {}                           
    return render(request, 'index.html', {'cidade' : cidade, 'data' : data})
