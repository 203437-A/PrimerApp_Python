from django.urls import re_path
#Importando vistas
from loadImage.views import ImageView
from loadImage.views import ImageViewDetail

urlpatterns = [
    re_path(r'^lista/$', ImageView.as_view()),    
    re_path(r'^lista/(?P<pk>\d+)$', ImageViewDetail.as_view()),    
]
