from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)  # Like a varchar
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name  # name to be shown when called


class TodoList(models.Model):

    task = models.CharField(max_length=250)  # a string
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))  # a date
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))  # a date
    category = models.ForeignKey(Category, default="General", on_delete=models.CASCADE)  # a foreignkey

    class Meta:
        ordering = ["-created"]  # ordering by the created field

    def __str__(self):
        return self.task  # name to be shown when called