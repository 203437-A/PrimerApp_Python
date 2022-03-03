
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from register.serializers import RegisterTableSerializer


from .serializers import RegisterSerializerNew
from rest_framework import generics
from rest_framework.permissions import AllowAny

#Create your views here.

class RegisterUser(APIView):
    permission_classes=[permissions.AllowAny]
    def post(self, request, format=None):
        serializer= RegisterTableSerializer(data=request.data, context={'request':request})
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterUserNew(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializerNew

