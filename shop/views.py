from django.shortcuts import render, redirect
from .models import Album
from .forms import AlbumForm
def home(request):
    postari = Album.objects.order_by('-id')
    return render (request, 'home.html', {'postari': postari})

def adauga(request):
    context ={}

    # create object of form
    form = AlbumForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    context['form']= form
    return render(request, "adauga.html", context)


def iarna(request):
    postari = Album.objects.filter(anotimp='Iarna').order_by('-id')
    return render (request, 'iarna.html', {'postari': postari})


def primavara(request):
    postari = Album.objects.filter(anotimp='Primavara').order_by('-id')
    return render (request, 'primavara.html', {'postari': postari})


def vara(request):
    postari = Album.objects.filter(anotimp='Vara').order_by('-id')
    return render (request, 'vara.html', {'postari': postari})


def toamna(request):
    postari = Album.objects.filter(anotimp='Toamna').order_by('-id')
    return render (request, 'toamna.html', {'postari': postari})


def altele(request):
    postari = Album.objects.filter(anotimp='Altele').order_by('-id')
    return render (request, 'altele.html', {'postari': postari})