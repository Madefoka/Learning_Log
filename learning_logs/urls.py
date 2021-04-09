"""Definiuje wzorce adresów URL dla learning_log"""

#from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Strona główna
    path('', views.index, name='index'),
    # Wyświetlenie wszystkich tematów
    path('topics/', views.topics, name='topics'),
    # Strona szczegółowa dotycząca pojedyńczego tematu
    path('topics/(<int:topic_id>)', views.topic, name='topic'),
    # Strona przeznaczona do dodawania nowgo tematu
    path('new_topic/', views.new_topic, name='new_topic'),
    # Strona przeznaczona do dodawania nowego wpisu
    path('new_entry/(<int:topic_id>)/', views.new_entry, name='new_entry'),
    #Strona przeznaczona do edycji wpisu.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
