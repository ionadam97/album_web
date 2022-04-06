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

