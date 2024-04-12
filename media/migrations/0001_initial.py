# Generated by Django 5.0.2 on 2024-04-12 07:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='medias', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png', 'webp', 'mp4', 'avi', 'mpeg4', 'mkv', 'pdf', 'doc', 'docx', 'gif'])], verbose_name='File')),
                ('file_type', models.CharField(choices=[('image', 'Image'), ('video', 'Video'), ('document', 'Document'), ('gif', 'Gif'), ('other', 'Other')], max_length=20, verbose_name='File Type')),
            ],
            options={
                'verbose_name': 'Media',
                'verbose_name_plural': 'Media',
            },
        ),
    ]