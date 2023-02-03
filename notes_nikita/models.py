from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

class Notes(models.Model):
    caption = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
    reminder = models.DateTimeField(null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Notes"