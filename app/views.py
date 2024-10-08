# from django.forms import model_to_dict
# from rest_framework.views import APIView
# from rest_framework.request import Request
# from rest_framework.response import Response
#
# from .models import Category, Author, Article, Comment
#
# class CategoryAPIView(APIView):
#     def get(self, request: Request, pk=None):
#         if not pk:
#             list_categories = []
#             categories = Category.objects.all()
#             for category in categories:
#                 list_categories.append({
#                     "id": category.id,
#                     "name": category.name,
#                 })
#             return Response(list_categories)
#         try:
#             category = Category.objects.get(pk=pk)
#             return Response(model_to_dict(category))
#         except:
#             return Response({"error": "Category not found"}, status=404)
#
# class AuthorAPIView(APIView):
#     def get(self, request: Request, pk=None):
#         if not pk:
#             list_authors = []
#             authors = Author.objects.all()
#             for author in authors:
#                 list_authors.append({
#                     "id": author.id,
#                     "last_name": author.last_name,
#                     "first_name": author.first_name,
#                 })
#             return Response(list_authors)
#         try:
#             author = Author.objects.get(pk=pk)
#             return Response(model_to_dict(author))
#         except:
#             return Response({"error": "Author not found"}, status=404)
#
# class ArticleAPIView(APIView):
#     def get(self, request: Request, pk):
#         if not pk:
#             list_articles = []
#             articles = Article.objects.all()
#             for article in articles:
#                 list_articles.append({
#                     "id": article.id,
#                     "title": article.title,
#                     "description": article.description,
#                     "created_at": article.created_at,
#                     "author": article.author.last_name,
#                     "category": f"{article.category.name} - {article.category.pk}",
#                 })
#             return Response(list_articles)
#         try:
#             article = Article.objects.get(pk=pk)
#             return Response(model_to_dict(article))
#         except:
#             return Response({"error": "Article not found"}, status=404)
#
# class CommentAPIView(APIView):
#     def get(self, request: Request, pk):
#         if not pk:
#             list_comments = []
#             comments = Comment.objects.all()
#             for comment in comments:
#                 list_comments.append({
#                     "id": comment.id,
#                     "comment_text": comment.comment_text,
#                     "author": f"{comment.author.last_name} - {comment.author.pk}",
#                     "article": comment.article.title,
#                     "published_date": comment.published_date,
#                 })
#             return Response(list_comments)
#         try:
#             comment = Comment.objects.get(pk=pk)
#             return Response(model_to_dict(comment))
#         except:
#             return Response({"error": "Comment not found"}, status=404)





from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Category, Author, Article, Comment


class CategoryAPIView(APIView):
    def get(self, request: Request, pk=None):
        if pk:
            # Agar `pk` mavjud bo'lsa, bitta kategoriya ma'lumotini qaytarish
            try:
                category = Category.objects.get(pk=pk)
                return Response(model_to_dict(category))
            except Category.DoesNotExist:
                return Response({"error": "Category not found"}, status=404)
        else:
            # Barcha kategoriyalarni ro'yxat ko'rinishida qaytarish
            categories = Category.objects.all().values("id", "name")
            return Response(list(categories))


class AuthorAPIView(APIView):
    def get(self, request: Request, pk=None):
        if pk:
            # Agar `pk` mavjud bo'lsa, bitta muallif ma'lumotini qaytarish
            try:
                author = Author.objects.get(pk=pk)
                return Response(model_to_dict(author))
            except Author.DoesNotExist:
                return Response({"error": "Author not found"}, status=404)
        else:
            # Barcha mualliflarni ro'yxat ko'rinishida qaytarish
            authors = Author.objects.all().values("id", "last_name", "first_name")
            return Response(list(authors))


class ArticleAPIView(APIView):
    def get(self, request: Request, pk=None):
        if pk:
            # Agar `pk` mavjud bo'lsa, bitta maqola ma'lumotini qaytarish
            try:
                article = Article.objects.get(pk=pk)
                article_data = {
                    "id": article.id,
                    "title": article.title,
                    "description": article.description,
                    "created_at": article.created_at,
                    "author": f"{article.author.first_name} {article.author.last_name}",
                    "category": article.category.name,
                    "image_url": article.image.url if article.image else None,
                }
                return Response(article_data)
            except:
                return Response({"error": "Article not found"}, status=404)
        else:
            # Barcha maqolalarni ro'yxat ko'rinishida qaytarish
            articles = Article.objects.all().values(
                "id", "title", "description", "created_at", "author__first_name", "author__last_name", "category__name"
            )
            return Response(list(articles))


class CommentAPIView(APIView):
    def get(self, request: Request, pk=None):
        if pk:
            # Agar `pk` mavjud bo'lsa, bitta izoh ma'lumotini qaytarish
            try:
                comment = Comment.objects.get(pk=pk)
                comment_data = {
                    "id": comment.id,
                    "comment_text": comment.comment_text,
                    "author": f"{comment.author.first_name} {comment.author.last_name}",
                    "article": comment.article.title,
                    "published_date": comment.published_date,
                }
                return Response(comment_data)
            except Comment.DoesNotExist:
                return Response({"error": "Comment not found"}, status=404)
        else:
            # Barcha izohlarni ro'yxat ko'rinishida qaytarish
            comments = Comment.objects.all().values(
                "id", "comment_text", "author__first_name", "author__last_name", "article__title", "published_date"
            )
            return Response(list(comments))
