from django.shortcuts import render
from .models import Event

# Create your views here.
def main (request):
    event = Event.objects
    return render (request, 'events/main.html', {'events':event})