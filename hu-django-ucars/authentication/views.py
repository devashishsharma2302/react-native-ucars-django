from __future__ import unicode_literals, absolute_import

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView

User = get_user_model()
from .permissions import IsUserOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Creates, Updates, and retrieves User accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,)
    authentication_classes = (TokenAuthentication, )

    def create(self, request, *args, **kwargs):
        self.serializer_class = CreateUserSerializer
        self.permission_classes = (AllowAny,)
        return super(UserViewSet, self).create(request, *args, **kwargs)



class UserImageAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


    def put(self, request):
        user = request.user
        user.image_path = request.data.get("image_path")
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)
