from django.shortcuts import render
from website.models import Instruments, Positions, ResearchArea, ResearchDetails, Publications, News


def home(request):
    reseachAreas = ResearchArea.objects.all()
    context = {
        'researches': reseachAreas,
    }
    return render(request, 'home.html', context)

def research(request):
    researches = ResearchDetails.objects.all()
    context = {
        'researches': researches,
    }
    return render(request, 'research.html', context)

def lab(request):
    instruments = Instruments.objects.all()
    context = {
        'instruments': instruments,
    }
    return render(request, 'lab.html', context)

def publications(request):
    publications = Publications.objects.all()
    context = {
        'publications': publications,
    }
    return render(request, 'publications.html', context)

def zonglin_chu(request):
    return render(request, 'zonglin_chu.html')

def members(request):
    positions = Positions.objects.all()
    context = {
        'positions': positions,
    }
    return render(request, 'members.html', context)

def Events(request):
    news = News.objects.all()
    context = {
        'news': news,
    }
    return render(request, 'events.html', context)

def news(request, slug):
    news = News.objects.get(slug=slug)
    context = {
        'news': news,
    }
    return render(request, 'news.html', context)