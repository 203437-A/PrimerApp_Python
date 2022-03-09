
from email.policy import HTTP
import os
from rest_framework.views import APIView
#Importación Response y status
from rest_framework.response import Response
from rest_framework import status
#Importación de serializer
from profileC.serializers import ProfileSerializer
from profileC.serializers import ProfileSerializerUser
#Importación de modelos
from profileC.models import ProfileModel
from django.contrib.auth.models import User

# Create your views here.

def get_user(pk):
  try:
    return User.objects.get(pk=pk)
  except User.DoesNotExist:
    return 404

def get_image(pk):
  try:
    return ProfileModel.objects.get(id_user=pk)
  except ProfileModel.DoesNotExist:
    return 404

class ImageView(APIView):

  def post(self, request):
    nameFile = request.data['name_img']
    id_user= request.data['id_user']
    user = get_user(id_user)
    user_img = get_image(id_user)
    if user!= 404:
      if user_img==404:
        serializer= ProfileSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
          serializer.create(nameFile, user)
          return Response('Succes', status=status.HTTP_200_OK)
        else:
          return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
      else: 
        return Response('Error el id es repetido', status=status.HTTP_400_BAD_REQUEST)
    else:
      return Response('Error, el ussuario no existe')

class ImageViewDetail(APIView):
  def get(self, request,pk,format=None):
    user_img = get_image(pk)
    if user_img != 404:
      serializer= ProfileSerializer(user_img)
      return Response(serializer.data, status.HTTP_200_OK)
    else:
      return Response('Error', status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, pk, format=None):
    nameFile = request.data['name_img']
    user_img= get_image(pk)
    stringFile= str(user_img.name_img)
    if user_img != 404:
      serializer= ProfileSerializerUser(user_img)
      try:
        os.remove('assets/'+stringFile)
      except:
        return Response('Error', status=status.HTTP_400_BAD_REQUEST)
      user_img.name_img=nameFile
      user_img.save()
      return Response ('Succes', status=status.HTTP_200_OK)
    else:
      return Response ('Error', status=status.HTTP_400_BAD_REQUEST)