#from django.contrib.auth.models import User
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        print("Serializer executing")
        model = User
        fields = ['username', 'alias']
        #fields = ['url', 'username', 'email', 'groups']
        #fields = ['name','address']
