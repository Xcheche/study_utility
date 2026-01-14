from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Homework(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    description = RichTextField()
    due = models.DateTimeField()
    is_finished = models.BooleanField(default=False)

    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Homework"
        verbose_name_plural = "Homeworks"
        ordering = ["-due"]