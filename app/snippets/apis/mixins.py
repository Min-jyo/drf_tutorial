from rest_framework import mixins, generics

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetListCreateAPIView(mixins.ListModelMixin,
                               mixins.CreateModelMixin,
                               generics.GenericAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SnippetRetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin,
                                          mixins.UpdateModelMixin,
                                          mixins.DestroyModelMixin,
                                          generics.GenericAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)