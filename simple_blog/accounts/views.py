from django.contrib.auth import get_user_model
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .serializers import UserSerializer

# Create your views here.

User = get_user_model()

class UserCreateAPIView(CreateAPIView):
    """
    post:
        Create new user instance. Returns username, email of the created user.
        parameters: [username, email, password]
    """

    serializer_class = UserSerializer

class UserListAPIView(ListAPIView):
    """
    get:
        Returns list of all exisiting users
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Returns the detail of a user instance
        parameters: [id]

    put:
        Update the detail of a user instance
        parameters: [id, username, email, password]

    delete:
        Delete a user instance
        parameters: [id]
    """

    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'


