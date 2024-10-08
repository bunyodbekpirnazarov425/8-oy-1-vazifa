from django.urls import path
from .views import CategoryAPIView, AuthorAPIView, ArticleAPIView, CommentAPIView


urlpatterns = [
        path('category/', CategoryAPIView.as_view()),
        path('category/<int:pk>', CategoryAPIView.as_view()),
        path('author/', AuthorAPIView.as_view()),
        path('author/<int:pk>', AuthorAPIView.as_view()),
        path('article/', ArticleAPIView.as_view()),
        path('article/<int:pk>', ArticleAPIView.as_view()),
        path('comment/', CommentAPIView.as_view()),
        path('comment/<int:pk>', ArticleAPIView.as_view()),
]
