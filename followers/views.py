from rest_framework import permissions, generics
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Followers
from .serializers import FollowersSerializer


class FollowersList(generics.ListCreateAPIView):
    """
    Displays a list of all the Followers and their information.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Followers.objects.all()
    serializer_class = FollowersSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowersDetail(generics.RetrieveDestroyAPIView):
    """
    Display Followers detail.
    The owner of the Followers can delete their Followers here.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Followers.objects.all()
    serializer_class = FollowersSerializer
