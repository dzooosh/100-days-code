from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    context = {
        'movies': [
            'gladiators',
            'top gun',
            'Avengers',
            'Casino'
        ]
    }
    return render(request, 'movies/index.html', context)