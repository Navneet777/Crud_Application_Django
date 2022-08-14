# Generated by Django 3.2.15 on 2022-08-14 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('short_description', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='media/')),
                ('status', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Approved', 'Approved')], max_length=300, null=True)),
                ('meta_title', models.CharField(max_length=150)),
                ('meta_description', models.TextField(blank=True)),
                ('meta_keyword', models.CharField(max_length=300)),
                ('og_title', models.TextField(blank=True)),
                ('og_description', models.CharField(max_length=300)),
                ('og_url', models.CharField(max_length=150)),
                ('canonical_url', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'news',
            },
        ),
    ]