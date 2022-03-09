from django.urls import re_path

#Importando vistas
from profileC.views import ImageView, ImageViewDetail, UserViewDetail

urlpatterns = [
    re_path(r'^profile/$', ImageView.as_view()),   
    re_path(r'^profile/(?P<pk>\d+)/$', ImageViewDetail.as_view()),
    re_path(r'^change_user/(?P<pk>\d+)/$', UserViewDetail.as_view()) 
]

