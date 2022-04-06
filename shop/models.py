from django.db import models
from django.forms import ModelForm

# Create your models here.
class Album(models.Model):
    vara= 'Vara'
    toamna = 'Toamna'
    iarna = 'Iarna'
    primavara = 'Primavara'
    altele = 'Altele'
    nume_anotimp = [
        (vara,'Vara'),
        (toamna,'Toamna'),
        (iarna,'Iarna'),
        (primavara,'Primavara'),
        (altele, 'Altele')
    ]
    title = models.CharField('Titlu', max_length=50)
    image = models.ImageField( upload_to='shop_images/')
    desc = models.TextField('text')
    anotimp = models.CharField(choices=nume_anotimp,
                               default=altele,
                               max_length=10,)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'toate postarile'
        verbose_name_plural = 'postari'