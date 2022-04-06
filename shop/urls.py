from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('adauga', views.adauga, name='adauga'),
    path('iarna', views.iarna, name='iarna'),
    path('primavara', views.primavara, name='primavara'),
    path('vara', views.vara, name='vara'),
    path('toamna', views.toamna, name='toamna'),
    path('altele', views.altele, name='altele'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
