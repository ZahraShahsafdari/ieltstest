# Generated by Django 5.2.4 on 2025-07-05 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ieltstest', '0003_wquestion_writingtext_wanswer_wquestion_writing_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='writingtext',
            name='writing_text',
        ),
        migrations.AddField(
            model_name='writingtext',
            name='writing_image',
            field=models.ImageField(null=True, upload_to='writing_images/'),
        ),
    ]
