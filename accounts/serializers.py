from rest_framework import serializers
from accounts.models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('phone', 'photo')


class UserCreateSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'first_name', 'last_name', 'password', 'profile')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'profile')
        read_only_fields = ('username',)

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')

        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()

        if hasattr(instance, 'profile'):
            profile = instance.profile
            profile.phone = profile_data.get('phone', profile.phone)
            profile.photo = profile_data.get('photo', profile.photo)
            profile.save()

        return instance
