from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Tag)