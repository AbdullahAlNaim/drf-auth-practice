from rest_framework import serializers
from blog.models import BlogPost
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class BlogPostSerializer(serializers.ModelSerializer):
    # auther = serializers.ReadOnlyField(source='auther.username')
    

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'body']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}} # ?

    # def create(self, validated_data):
    #         user = User(
    #         username=validated_data['username']
    #     )
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user


        # def to_internal_value(self, validated_data):
        #     raw_password = validated_data.pop('password')
        #     user = super().to_internal_value(validated_data)
        #     user.set_password(raw_password)  # Hash the raw password
        #     return user


    # def create(self, validated_data):
    #     user = super(UserSerializer, self).create(validated_data)
    #     user.set_password(validated_data['password'])
    #     user.save()
        # return user

        # def validate_password(self,value):
        #     return make_password(value)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(
            username=validated_data['username'], 
            email=validated_data['email']
        )
        user.set_password(password)  # Hash the password before saving
        user.save()
        return user

        # def perform_create(self, serializer):
        #     new_user = User.objects.create(username=self.request.data.get('username'))
        #     new_user.set_password(self.request.data.get('password'))
        #     serializer.save(password=user.password)

        # def create(self, validated_date):
        #     password = validated_data.pop('password')
        #     user = User(**validated_data)
        #     user.make_password(password)
        #     user.save()
        #     return user

        # user = User.objects.create(
        #     email=validated_data['email'],
        #     username=validated_data['username'],
        #     password=make_password(validated_data['password'])
        # )

        # def create(self, validated_data):
        #     validated_data['password'] = make_password(validated_data['password'])
        #     return super(UserSerializer, self).create(validated_data)

        # def create(self, validated_data):
        #     user = super().create(validated_data)
        #     user.set_password(validated_data['password'])
        #     user.save()
        #     return user
