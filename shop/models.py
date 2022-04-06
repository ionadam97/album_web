from django.db import models
from django.forms import ModelForm

# Create your models here.
class Album(models.Model):
    title = models.CharField('Titlu', max_length=50)
    image = models.ImageField( upload_to='shop_images/')
    desc = models.TextField('text')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'toate postarile'
        verbose_name_plural = 'postari'