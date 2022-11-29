# from django.contrib.auth.models import User, Group
from instagramcloneapi.models import  User, Post, Profile
from rest_framework import status
from rest_framework.response import Response
from instagramcloneapi.permissions import IsOwnerOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from instagramcloneapi.serializers import UserSerializer, PostSerializer, ProfileSerializer
from rest_framework.views import APIView
from rest_framework import routers, viewsets
from django.core import serializers
import json
import jwt

class CustomResponse:
    def error(message, status):
        return Response({
            'status': 'failed',
            'messsage': message
        }, status=status)

    def success(message, data, status):
        return Response({
            'status': 'success',
            'messsage': message,
            'data': data
        }, status=status)

class JWT_TOEKN:
    def CreateJWT(payload):
        return jwt.encode(payload, 'secretKey', algorithm='HS256')

    def DecodeJWT(token):
        decoded = jwt.decode(token, 'secretKey', algorithms=['HS256'])
        return decoded

class RegisterView(APIView):

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        phoneNumber = data["phoneNumber"]
        email = data["email"]
        password = data['password']
        token = JWT_TOEKN.CreateJWT({"email": email})
        
        data_obj = {"phoneNumber": phoneNumber, "email": email, "password": password, "token": token}

        user = UserSerializer(data=data_obj)
        
        if user.is_valid():
            user.save()
            instance = user.data
            return Response({"status": "success", "data": instance, "token": token})
        return Response(data="Failed to save", status=400)


class LoginView(APIView):
     
     def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        password = data['password']
        phoneNumber = data["phoneNumber"]
        email = data["email"]
        try:
            user = User.objects.get(email= email, phoneNumber = phoneNumber, password = password)
            token = JWT_TOEKN.CreateJWT({"email": email})
            if user:
                return Response({"status": "success", "data": {
                    "id": user.id,
                    "phoneNumber": user.phoneNumber,
                    "email": user.email,
                    "created": user.created,
                    "token": token
                }}, status=200)
        except User.DoesNotExist:
            return Response({
                "status": "failed",
                "message": "User not found"
            }, status=400)
    
        
class UserFeeds(APIView):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    

class PostView(APIView):
   def post(self, request, *args, **kwargs):
        try:
            title = request.data["title"]
            description = request.data["description"]
            userId = request.data["userId"]
            file = request.data['file']
        except:
            return CustomResponse.error('Enter proper input', 404)
        try:
            serializer = PostSerializer(data={"title": title, "description": description, "image": file})
            print(title, description, file)
            user = User.objects.get(id=userId)

        except:
            return CustomResponse.error('User not found', 400)

        if serializer.is_valid():
            try:
                print("1")
                serializer.save(user=user, image = file)
                print("2")
                return CustomResponse.success('Profile created', serializer.data, 201)
            except:
                print(serializer.errors, serializer.error_messages)
                return CustomResponse.error('profile already created for this user', 404)
        else:
            print(userId)
            print(serializer.errors)
            return CustomResponse.error('profile already created for this user', 404)
    
   
class ProfileView(APIView):

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id', None)
        try: 
            profile = Profile.objects.get(id=id)
            serializer = ProfileSerializer(data=profile)
            print('profile', profile.image)
            return Response({
                "status": "success",
                "data": {
                    "id": profile.id,
                    "image": str(profile.image),
                    "username": profile.username,
                    "name": profile.name
                }
            }, status=200)
        except Profile.DoesNotExist:
            return CustomResponse.error('Profile not found', 400)

    def post(self, request, *args, **kwargs):

        try:
            file = request.data['file']
            name = request.data["name"]
            userId = request.data["userId"]
            username = request.data["username"]
        except:
            return CustomResponse.error('Enter proper input', 404)
        try:
            serializer = ProfileSerializer(data={"username": username, "name": name, "image": file})
            user = User.objects.get(id=userId)

        except:
            return CustomResponse.error('User not found', 400)

        if serializer.is_valid():
            try:
                serializer.save(user=user, image = file)
                return CustomResponse.success('Profile created', serializer.data, 201)
            except:
                return CustomResponse.error('profile already created for this user', 404)
        else:
            return CustomResponse.error('profile already created for this user', 404)

    def put(self, request, *args, **kwargs):
        print("put")
        instance = self.get_object()
        instance.name = request.data.get("name")
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)