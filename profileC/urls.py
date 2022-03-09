from django.urls import re_path

#Importando vistas
from profileC.views import ImageView

urlpatterns = [
    re_path(r'^profile/$', ImageView.as_view()),   

]

