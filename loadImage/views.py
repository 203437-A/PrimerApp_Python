
import datetime
import os
from rest_framework.views import APIView
#Importación de modelo
from loadImage.models import ImageModel
#Importación de serializers
from loadImage.serializers import ImageSerializer
from loadImage.serializers import ImageSerializerNameImage
#Importación Response y status
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ImageView(APIView):

  def get(self, request, format=None):
    querySet = ImageModel.objects.all()
    serializer= ImageSerializer(querySet,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request):
    nameFile = request.data['name_img']
    serializer= ImageSerializerNameImage(data=request.data, context={'request':request})
    if serializer.is_valid():
      serializer.create(nameFile)
      return Response("Succes", status=status.HTTP_201_CREATED)
    else:
      return Response("Error", status=status.HTTP_400_BAD_REQUEST)

class ImageViewDetail(APIView):

  def get_object(self, pk):
    try:
      return ImageModel.objects.get(pk=pk)
    except ImageModel.DoesNotExist:
      return 404

  def get(self, request, pk, format=None):
    idResponse = self.get_object(pk)

    if idResponse != 404:
      serializer = ImageSerializer(idResponse, context= {'request': request})
      return Response(serializer.data, status=status.HTTP_200_OK)
    else:
      return Response('id no encontrado', status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, pk, format=None):
    idResponse = self.get_object(pk)

    if idResponse !=404:
      serializer= ImageSerializerNameImage(idResponse, data=request.data, context={'request': request})

      if serializer.is_valid():
        try:
          os.remove('assets/'+ str(idResponse.name_img))
        except os.error:
          print('Error')
        
        idResponse.name_img=(request.data['name_img'])
        idResponse.url_image='http://localhost:8000/assets/'+str(request.data['name_img'])  
        idResponse.format_img=str(request.data['name_img']).split(".")[1]         
        idResponse.edited=datetime.datetime.now()
        idResponse.save()
        return Response("Succes", status=status.HTTP_200_OK)
      else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
      return Response('id no encontrado', status=status.HTTP_400_BAD_REQUEST)


  def delete(self, request, pk, format=None):
    idResponse = self.get_object(pk)

    if idResponse != 404:
      serializer= ImageSerializerNameImage(idResponse, data= request.data , context={'request': request})
      if serializer.is_valid():    
        try:
          os.remove('assets/'+ str(idResponse.name_img))
        except os.error:
          print('Error')
        idResponse.delete()
        return Response('Succes', status=status.HTTP_200_OK)
      else:
        return Response(serializer.errors, status=status.HTTP_200_OK)
    else:
      return Response('id no encontrado', status=status.HTTP_400_BAD_REQUEST)