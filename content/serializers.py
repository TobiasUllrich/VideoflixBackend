from rest_framework import serializers
from django.contrib.auth.models import User

#Users-Serializer (defines the API)
class UsersSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id','username','email'] #Oder '__all__' wenn man alle Felder haben will