from rest_framework import serializers
from account.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']

    def update(self, instance, validated_data):
        # Solo permite la actualización para superusuarios
        if self.context['request'].user.is_superuser:
            instance.username = validated_data.get('username', instance.username)
            instance.email = validated_data.get('email', instance.email)
            instance.save()
            return instance
        else:
            raise serializers.ValidationError("No tienes permisos para realizar esta acción.")