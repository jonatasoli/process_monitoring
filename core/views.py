from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from . import serializers
from . import models
from . import permissions


class StatusProcessViewSet(viewsets.ViewSet):
    """Process API ViewSet"""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.StatusProcessSerializer
    queryset = models.StatusProcess.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)

    def list(self, request):
        """List Process."""

        process_list = models.StatusProcess.objects.all().filter(user_profile=self.request.user)
        a_viewset = []
        count = 0

        while count < process_list.count():
            a_viewset.append(process_list.values()[count])
            count += 1

        return Response({'message': 'processos', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new process."""

        serializer = serializers.StatusProcessSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user_profile=self.request.user)
            name = serializer.data.get('id_process')
            message = 'Processo {0} criado!'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """Deleting an object."""

        process = models.StatusProcess.objects.all().filter(pk=kwargs['pk'])
        id_process = process.values()[0]['id_process']

        process.delete()

        message = 'Processo {0} deletado!'.format(id_process)

        return Response({'message': message})


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
