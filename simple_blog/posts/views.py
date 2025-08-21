from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

)
from rest_framework.response import Response
from .models import Post, Comment

from .serializers import (
    PostCreateUpdateSerializer, PostListSerializer, PostDetailSerializer, CommentSerializer, CommentCreateUpdateSerializer
)

from django.shortcuts import get_object_or_404

from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from .permissions import IsOwnerOrReadOnly

class CreatePostAPIView(CreateAPIView):
    """
    post:
        Creates a new post instance. Returns created post data

        parameters: [title, body, description, image]
    """
    permission_classes = [
        IsAuthenticated,
    ]

    serializer_class = PostCreateUpdateSerializer

    def post(self, request, *args, **kwargs):
        serializer = PostCreateUpdateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=200)
        else:
            return Response({"errors": serializer.errors}, status=400)


class ListPostAPIView(ListAPIView):
    """
    get:
        Returns a list of all existing posts
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class DetailPostAPIView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Returns the details of a post instance. Searches post using slug field.

    put:
        Updates an existing post. Returns updated post data

        parameters: [slug, title, body, description, image]

    delete:
        Delete an existing post

        parameters = [slug]
    """
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    lookup_field = "slug"
    serializer_class = PostDetailSerializer

class ListCommentAPIView(CreateAPIView):
    """
    get:
        Returns the list of comments on a particular post
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        comments = Comment.objects.filter(parent=post)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=200)


class CreateCommentAPIView(CreateAPIView):
    """
    post:
        Create a comment instnace. Returns created comment data

        parameters: [slug, body]

    """
    permission_classes = [IsAuthenticated]
    serializer_class = CommentCreateUpdateSerializer

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        serializer = CommentCreateUpdateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user, parent=post)
            return Response(serializer.data, status=200)
        else:
            return Response({"errors": serializer.errors}, status=400)


class DetailCommentAPIView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Returns the details of a comment instance. Searches comment using comment id and post slug in the url.

    put:
        Updates an existing comment. Returns updated comment data

        parameters: [parent, author, body]

    delete:
        Delete an existing comment

        parameters: [parent, author, body]
    """

    #permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    lookup_fields = ["parent", "id"]
    serializer_class = CommentCreateUpdateSerializer

    def get_object(self):
        queryset = self.get_queryset()  # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        # for field in self.lookup_fields:
        #     if self.kwargs[field]: # Ignore empty fields.
        #         filter[field] = self.kwargs[field]
        parent_id = Post.objects.get(slug=self.kwargs["slug"]).id
        filter["parent"] = parent_id
        filter["id"] = self.kwargs["id"]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj
