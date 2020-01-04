from django.contrib import admin
from .models import TodoList
from .models import Category


# Register your models here.
admin.site.register(TodoList)
admin.site.register(Category)