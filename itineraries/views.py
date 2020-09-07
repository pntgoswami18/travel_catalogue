from django.shortcuts import render

# Create your views here.


def itineraries(request):
    return render(request, 'itineraries/itineraries.html',)
