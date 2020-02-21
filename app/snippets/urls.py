from django.urls import path, include

# from snippets import views
# from snippets import apis
from rest_framework.routers import DefaultRouter

from snippets.apis import mixins, viewsets
from snippets.apis import generic

app_name = 'snippets'

router = DefaultRouter()
router.register(r'snippets', viewsets.SnippetViewSet)

urlpatterns_viewset = [
    path('snippets/', viewsets.SnippetViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('snippets/<int:pk>/', viewsets.SnippetViewSet.as_view({
        'get': 'retrieve',
        'patch': 'partial_update',
        'delete': 'destroy',
    })),
]

urlpatterns_api_view = [
    path('snippets/', generic.SnippetListCreateAPIView.as_view()),
    path('snippets/<int:pk>/', generic.SnippetRetrieveUpdateDestroyAPIView.as_view())
]

urlpatterns = [
    path('api-view/', include(urlpatterns_api_view)),
    path('viewsets/', include(urlpatterns_viewset)),
    path('router/', include(router.urls)),
]