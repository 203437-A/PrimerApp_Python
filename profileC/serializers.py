

from rest_framework import serializers

# Importación de modelos
from profileC.models import ProfileModel 
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('__all__')

    def create(self, nameFile, user):
        ProfileModel.objects.create(
            name_img= nameFile,
            id_user=user
        )

class ProfileSerializerUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        