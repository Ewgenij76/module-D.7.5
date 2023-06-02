from django.forms import ModelForm
from .models import Post, Category, Author

class NewsEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']

class NewsAddForm(ModelForm):
    categories = Category.objects.all()
    author = Author.objects.all()

    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'categories', 'post_type',]

class ArticleAddForm(ModelForm):
    categories = Category.objects.all()
    author = Author.objects.all()

    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'categories', 'post_type']
