from django.db import models
from django.utils import timezone


CHOICES = (
        ('NEWS', 'News'),
        ('ARTICAL', 'Artical'),
        ('BLOG', 'Blog'),
        ('FAQ', 'Faq'),
        ('LEGAL TERMS', 'Legal Terms'),
    )

published_options = ((True, 'Yes'), (False, 'No'))

class Category(models.Model):
    class Meta:
        db_table = 'category'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=300, choices = CHOICES)
    published = models.BooleanField(max_length=300, choices = published_options)

    def __str__(self):
        return self.name
    