# Generated by Django 3.2.15 on 2022-08-14 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category_management', '0002_alter_category_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='published',
            field=models.BooleanField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=300),
        ),
    ]
