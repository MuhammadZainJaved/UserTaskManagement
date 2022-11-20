# from rest_framework import serializers
# from .models import user_Account
# from django.core import exceptions
# from django.contrib.auth import authenticate


# class RegisterSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

#     class Meta:
#         model = user_Account
#         fields = '__all__'
#         extra_kwargs = {
#             'password': {"write_only": True}
#         }

#     def save(self, obj):
#         account = user_Account(
#             email=obj.data.get('email'),
#             username=obj.data.get('username'),
#         )

#         password = obj.data.get('password')
#         password2 = obj.data.get('password2')

#         if password != password2:
#             raise serializers.ValidationError({'password': "passwords must match"})
#         account.set_password(password)
#         account.save()
#         return account


# class LoginSerializer(serializers.Serializer):
#     email = serializers.CharField()
#     password = serializers.CharField()

#     def validate(self, data):
#         email = data.get('email', '')
#         password = data.get('password', '')

#         if email and password:
#             user = user_Account.objects.get(email=email)
#             if user.check_password(password):

#             # user = authenticate(email=email, password=password)
#             # if user:

#                 if user.is_active:
#                     return user
#                 else:
#                     msg = "user is deactivated"
#                     raise exceptions.ValidationError(msg)

#             else:
#                 msg = "unable to login with given credentials"
#                 raise exceptions.ValidationError(msg)
#         else:
#             msg = "Must provide email and password"
#             raise exceptions.ValidationError(msg)


# class UserDataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_Account
#         fields = ['email', 'username', 'is_verified', 'userCode']
