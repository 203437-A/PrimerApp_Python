
from django.urls import re_path
#Importando vistas
from register.views import RegisterUser

urlpatterns = [
    re_path(r'^', RegisterUser.as_view()),   
]
