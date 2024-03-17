#holateam

#from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from app_lugares_seguros.models import UserProfile
from app_lugares_seguros.serializers import UserProfileSerializer

#USER
class RetrieveUserProfile(APIView):
	permission_classes=(AllowAny,)
	
	def get(self, request):
		user_list= UserProfile.objects.all().values ()
		serializer=UserProfileSerializer(user_list, many=True)
		return Response(serializer.data)
	
class CreateUserProfile(APIView):
	permission_classes=(AllowAny,)
	


	def post(self,request):
		#validación:
		data=request.data
		serializer=UserProfileSerializer(data=data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data ,status=status.HTTP_201_CREATED)
	
# Create your views here.
