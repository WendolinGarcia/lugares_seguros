from rest_framework import serializers

from app_lugares_seguros.models import UserProfile 

class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model=UserProfile
		fields= ('name', 'lastname', 'age', 'email', 'password')