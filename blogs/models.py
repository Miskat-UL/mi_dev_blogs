from django.db import models
from django.db.models.deletion import SET_NULL


class Tag(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    TYPE_CHOICES = [
        ('category', 'Category'),
        ('subcategory', 'Subcategory'),
        ('tag', 'Tag')
    ]
    name = models.CharField(max_length=100)
    # slug = models.SlugField()
    type = models.CharField(choices=TYPE_CHOICES, max_length=20)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50)
    author_img = models.ImageField(upload_to="media")
    email = models.EmailField()
    institution = models.CharField(max_length=100 , blank=True,null=True)
    study_subject = models.CharField(max_length=100, blank=True, null=True)
    current_year = models.CharField(max_length=50, blank=True, null=True)
    github = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    Twitter = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    comment_body = models.CharField(max_length=500)
    react = models.CharField(max_length=100, blank=True, null=True)
    comment_reply = models.CharField(max_length=500)
    comment_time_created = models.DateTimeField(auto_now_add=True)
    comment_author = models.ForeignKey(Author, on_delete=SET_NULL, null=True)


class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=10000)
    img = models.ImageField(upload_to="media")
    author = models.ForeignKey(Author, on_delete=SET_NULL,null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    react = models.IntegerField(blank=True, null=True)
    comment = models.ManyToManyField(Comment)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


