from django.shortcuts import render

# Create your views here.
def index(req):
    return  render(req, 'index.html')

def foot(req):
    return  render(req, 'football.html')

def basc(req):
    return render(req, 'bascetball.html')

def ten(req):
    return render(req, 'tenis.html')

def sportsmen(req, sport, id):
    footballs = [
        {'name':'Sergio Ramos', 'pic':'img/fut_1.jpg', 'picsport': 'img/ball.jpg',
        'desc':'забил 10 голов, играет за ЦСК.'},
        {'name': 'Вася Аршавин', 'pic': 'img/fut_2.jpg', 'picsport': 'img/ball.jpg',
         'desc': 'забил 20 голов, играет за Спартак.'},
        {'name': 'Дима Пипкин', 'pic': 'img/fut_3.jpg', 'picsport': 'img/ball.jpg',
         'desc': 'забил 15 голов, играет за Динамо.'},
    ]
    data = {}
    if sport == 'football':
        data = {'name':footballs[id]['name'],
                'pic':footballs[id]['pic'],
                'picsport':footballs[id]['picsport'],
                'desc':footballs[id]['desc'],}

    return render(req, 'sportsmen.html', data)


