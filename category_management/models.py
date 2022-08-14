from django.db import models
from django.utils import timezone


CHOICES = (
        ('NEWS', 'News'),
        ('ARTICAL', 'Artical'),
        ('BLOG', 'Blog'),
        ('FAQ', 'Faq'),
        ('LEGAL TERMS', 'Legal Terms'),
    )
PUBLISHED_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        )
class Category(models.Model):
    class Meta:
        db_table = 'category'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=300, choices = CHOICES)
    published = models.CharField(max_length=300, choices = PUBLISHED_CHOICES)

    def __str__(self):
        return self.name
    