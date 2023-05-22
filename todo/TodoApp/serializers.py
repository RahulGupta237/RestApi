from rest_framework import serializers
from TodoApp.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
  # We are writing this becoz we need confirm password field in our Registratin Request
  password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
  is_admin= serializers.BooleanField(default=False)
 
  class Meta:
    model = User
    #fields=['email', 'name', 'password', 'password2', 'tc']
    fields = ['email','name','mobile_number','password','password2','is_admin']

    extra_kwargs={
      'password':{'write_only':True},
     
    }

  # Validating Password and Confirm Password while Registration
  def validate(self, attrs):
    password = attrs.get('password')
    password2 = attrs.get('password2')
    if password != password2:
      raise serializers.ValidationError("Password and Confirm Password doesn't match")
    return attrs
  
  def create(self, validate_data):
      is_superuser = self.validated_data.pop('is_admin', False)
      print("rahull",is_superuser)
      if is_superuser:
        return User.objects.create_superuser(**validate_data)
     
      return User.objects.create_user(**validate_data)


class UserLoginSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    model = User
    fields = ['email', 'password']


class UserProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'email','name', "mobile_number"]



class EditUserProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['email','name', "mobile_number"]
