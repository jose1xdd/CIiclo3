from rest_framework import serializers
from medicli.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password','name', 'email']

        def create(self, validated_data):
            userInstance = User.objects.create(**validated_data)
            return userInstance

        def to_representation(self, obj):
            user = User.objects.get(id=obj.id)
            return {
                'username': user.username,
                'password': user.password,
                'name':user.name, 
                'email': user.email,
            }
