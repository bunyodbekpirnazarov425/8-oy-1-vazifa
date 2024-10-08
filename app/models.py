from tkinter.constants import CASCADE

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Author(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    author_image = models.ImageField(upload_to='image/', blank=True, null=True)

    def __str__(self):
        return self.last_name

class Article(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/', blank=True, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user_email = models.EmailField()
    comment_text = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.article.title}"

    class Meta:
        ordering = ['-published_date'] # bu kod qo'shilgan kommentlarni vaqtiga qarab saralaydi