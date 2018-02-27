from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from . import serializers
from . import models
from . import permissions

# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework.permissions import IsAuthenticated


class StatusProcessViewSet(viewsets.ViewSet):
    """Process API ViewSet"""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.StatusProcessSerializer
    queryset = models.StatusProcess.objects.all()
    # permission_classes = (permissions.PostOwnStatus, IsAuthenticated)

    def list(self, request):
        """List Process."""

        serializer = serializers.StatusProcessSerializer

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)'
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new process."""

        serializer = serializers.StatusProcessSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Deleting an object."""

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, creating and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email', 'url')


class LoginViewSet(viewsets.ViewSet):
    """Checks e-mail and password and returns an auth token."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token."""

        return ObtainAuthToken().post(request)
