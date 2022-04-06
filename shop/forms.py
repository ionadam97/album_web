from .models import Album
from django.forms import ModelForm, TextInput, Textarea, FileInput



class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'desc', 'image','anotimp']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'introduceti titlu'
            }),
            'desc': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'introduceti descrierea'
            }),
            'image': FileInput(attrs={
                'class': 'form-control',

            }),
        }