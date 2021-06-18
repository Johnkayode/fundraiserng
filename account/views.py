from django.shortcuts import get_object_or_404, render

from rest_framework import generics, status
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import CustomUser
from .permissions import IsAuthenticated_
from .serializers import ChangePasswordSerializer, UserDashboardSerializer, UserSerializer, ConfirmAccountSerializer, UserLoginSerializer, UserDashboardSerializer


# List and Create vendors
class CreateAccount(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
   
# Confirm user account
class ConfirmAccount(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ConfirmAccountSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

    # Handle cases where confirmation code is not attached to an account
        
        try:
            user = CustomUser.objects.get(
                confirmation_code=serializer.data["confirmation_code"]
            )
        except CustomUser.DoesNotExist:
            return Response(
                {"detail": "User account does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )
    
        if user.is_active:
            return Response(
                {"detail": "User account already confirmed!"},
                status=status.HTTP_400_BAD_REQUEST,
            )


        

        # confirm account
        user.is_active = True
        user.save()
        
        return Response(
              {"detail": "Account confirmed successfully!"}, status=status.HTTP_200_OK
        )

#Login User
class LoginUser(CreateAPIView):

    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_object_or_404(CustomUser, email=serializer.data['email'])
        user = {
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'token' : serializer.data['token'],
        }

        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'user': user
        }

        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)

class ChangePassword(generics.GenericAPIView):
    
    permission_classes = (IsAuthenticated_,)
    serializer_class = ChangePasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
              {"detail": "Password changed successfully!"}, status=status.HTTP_200_OK
        )

class MyProfileDashboard(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated_,)


    def get(self, request):
        serializer = UserDashboardSerializer(self.request.user)
        return Response(serializer.data)







def reset_password(request):
    pass

def change_password(request):
    pass