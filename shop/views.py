from django.shortcuts import render, redirect
from .models import Album
from .forms import AlbumForm
def home(request):
    postari = Album.objects.all()
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
    postari = Album.objects.filter(title='ttj').order_by('title')
    return render (request, 'iarna.html', {'postari': postari})

def primavara(request):
    postari = Album.objects.all()
    return render (request, 'primavara.html', {'postari': postari})

def vara(request):
    postari = Album.objects.all()
    return render (request, 'vara.html', {'postari': postari})

def toamna(request):
    postari = Album.objects.all()
    return render (request, 'toamna.html', {'postari': postari})