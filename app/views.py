from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Category, Author, Article, Comment

class CategoryAPIView(APIView):
    def get(self, request: Request, pk=None):
        if not pk:
            list_categories = []
            categories = Category.objects.all()
            for category in categories:
                list_categories.append({
                    "id": category.id,
                    "name": category.name,
                })
            return Response(list_categories)
        try:
            category = Category.objects.get(pk=pk)
            return Response(model_to_dict(category))
        except:
            return Response({"error": "Category not found"}, status=404)

class AuthorAPIView(APIView):
    def get(self, request: Request, pk=None):
        if not pk:
            list_authors = []
            authors = Author.objects.all()
            for author in authors:
                list_authors.append({
                    "id": author.id,
                    "last_name": author.last_name,
                    "first_name": author.first_name,
                })
            return Response(list_authors)
        try:
            author = Author.objects.get(pk=pk)
            return Response(model_to_dict(author))
        except:
            return Response({"error": "Author not found"}, status=404)

class ArticleAPIView(APIView):
    def get(self, request: Request, pk):
        if not pk:
            list_articles = []
            articles = Article.objects.all()
            for article in articles:
                list_articles.append({
                    "id": article.id,
                    "title": article.title,
                    "description": article.description,
                    "created_at": article.created_at,
                    "author": article.author.last_name,
                    "category": f"{article.category.name} - {article.category.pk}",
                })
            return Response(list_articles)
        try:
            article = Article.objects.get(pk=pk)
            return Response(model_to_dict(article))
        except:
            return Response({"error": "Article not found"}, status=404)

class CommentAPIView(APIView):
    def get(self, request: Request, pk):
        if not pk:
            list_comments = []
            comments = Comment.objects.all()
            for comment in comments:
                list_comments.append({
                    "id": comment.id,
                    "comment_text": comment.comment_text,
                    "author": f"{comment.author.last_name} - {comment.author.pk}",
                    "article": comment.article.title,
                    "published_date": comment.published_date,
                })
            return Response(list_comments)
        try:
            comment = Comment.objects.get(pk=pk)
            return Response(model_to_dict(comment))
        except:
            return Response({"error": "Comment not found"}, status=404)