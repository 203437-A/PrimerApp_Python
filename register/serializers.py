
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterTableSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ('password','username','email')

    username = serializers.CharField(
        required=True, 
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    email = serializers.EmailField(
        required =True, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password= serializers.CharField(write_only=True, required=True)

    def create(self, validate_data):
        usuario = User.objects.create(
            username=validate_data['username'],
            email=validate_data['email'],
        )
        usuario.set_password(validate_data['password'])
        usuario.save()
        return usuario

