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

