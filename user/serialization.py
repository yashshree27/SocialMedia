from user.models import users_new
from rest_framework import serializers

class serializerClass(serializers.ModelSerializer):
    class Meta:
        model= users_new
        fields= '__all__'