# Generated by Django 3.2.15 on 2022-08-14 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='type',
            field=models.CharField(choices=[('NEWS', 'News'), ('ARTICAL', 'Artical'), ('BLOG', 'Blog'), ('FAQ', 'Faq'), ('LEGAL TERMS', 'Legal Terms')], max_length=300),
        ),
    ]
