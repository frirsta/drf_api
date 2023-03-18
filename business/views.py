from rest_framework import filters, generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import BusinessProfile
from .serializers import BusinessProfileSerializer


class BusinessProfileList(generics.ListCreateAPIView):
    """
    Displays a list of all the Business Profiles and their information.
    Filterset_fields Can find who follows a specific user.
    The filterset_fields can also find what Business Profiles are
    followed by a specific user.
    """
    serializer_class = BusinessProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = BusinessProfile.objects.all()
    filter_backends = [
        filters.SearchFilter,
    ]
    search_fields = ['owner__username']

    def perform_create(self, serializer):
        serializer.save(owner.self.request.user)


class BusinessProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Display account detail.
    The owner of the account can edit and delete their account here.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BusinessProfileSerializer
    queryset = BusinessProfile.objects.all()
