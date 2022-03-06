from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# req -> res / req handler or action

def yowaddup(req):
  x = 1
  y = 2
  return render(req, 'yo.html', {'name': 'Ryan'})