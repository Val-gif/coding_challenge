from rest_framework import routers
from .views import AuthorViewSet, BookList
from django.urls import path, include

router = routers.SimpleRouter()
router.register('authors', AuthorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('books/', BookList.as_view()),
    path('books/<int:pk>', BookList.as_view())
]

