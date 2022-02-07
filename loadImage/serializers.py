
from rest_framework import serializers

# Importación de modelos
from loadImage.models import ImageModel

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ('__all__')
        
class ImageSerializerNameImage(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ('name_img',)

    def create(self, nameFile):
        nameFileString= str(nameFile)
        formatExtension = nameFileString.split(".")[1]
        urlImage= 'http://localhost:8000/assets/'+ nameFileString
        image = ImageModel.objects.create(name_img=nameFile, format_img=formatExtension, url_img=urlImage)

