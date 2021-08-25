from django.http import JsonResponse
from . import serializers
from .models import Forest
# DRF
from rest_framework.views import APIView
from rest_framework import generics,permissions,authentication
# from auth_token.authentication import TokenAuthentication
from auth_token.permissions import IsAuthenticated
from auth_token.renderers import Renderer
from auth_token.authentication import UserAuthentication
class HelloView(APIView):
    """
        Returns a list of Categories available
    """
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    renderer_classes = (Renderer,)

    def get(self, request):
        return JsonResponse({'Hello':'View'})
    
class ForestCreateView(generics.CreateAPIView):
    queryset = Forest.objects.all()
    serializer_class = serializers.ForestSerializer
    permission_classes = (permissions.AllowAny,)
    renderer_classes = (Renderer,)

class ForestListView(generics.ListAPIView):
    # queryset = Forest.objects.all().order_by('name')
    serializer_class = serializers.ForestSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (UserAuthentication,) # already provided in settings file
    renderer_classes = (Renderer,)
    def get_queryset(self):
        user = Forest.objects.filter(name=self.request.user).order_by('name')
        return user