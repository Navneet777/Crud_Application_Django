from django.db import models

STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        )

class FAQ(models.Model):
    class Meta:
        db_table = 'faq'

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
    
    def __str__(self):
        return self.title

