from django.db import models
from django.utils import timezone


CHOICES = (
        ('NEWS', 'News'),
        ('ARTICAL', 'Artical'),
        ('BLOG', 'Blog'),
        ('FAQ', 'Faq'),
        ('LEGAL TERMS', 'Legal Terms'),
    )

STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
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
class News(models.Model):
    class Meta:
        db_table = '_news'

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    short_description = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media/')
    status = models.CharField(max_length=300, choices = STATUS_CHOICES,null=True,blank=True)
    meta_title = models.CharField(max_length=150)
    meta_description = models.TextField(blank = True)
    meta_keyword = models.CharField(max_length=300)
    og_title = models.TextField(blank = True)
    og_description = models.CharField(max_length=300)
    og_url = models.CharField(max_length=150)
    canonical_url = models.TextField(blank = True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.title
class FAQ(models.Model):
    class Meta:
        db_table = '_faq'

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    short_description = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media/')
    status = models.CharField(max_length=300, choices = STATUS_CHOICES,null=True,blank=True)
    meta_title = models.CharField(max_length=150)
    meta_description = models.TextField(blank = True)
    meta_keyword = models.CharField(max_length=300)
    og_title = models.TextField(blank = True)
    og_description = models.CharField(max_length=300)
    og_url = models.CharField(max_length=150)
    canonical_url = models.TextField(blank = True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.title
class Blog(models.Model):
    class Meta:
        db_table = '_blog'

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    short_description = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media/')
    status = models.CharField(max_length=300, choices = STATUS_CHOICES,null=True,blank=True)
    meta_title = models.CharField(max_length=150)
    meta_description = models.TextField(blank = True)
    meta_keyword = models.CharField(max_length=300)
    og_title = models.TextField(blank = True)
    og_description = models.CharField(max_length=300)
    og_url = models.CharField(max_length=150)
    canonical_url = models.TextField(blank = True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.title