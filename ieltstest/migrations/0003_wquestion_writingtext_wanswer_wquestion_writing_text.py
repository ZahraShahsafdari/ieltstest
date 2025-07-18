# Generated by Django 5.2.4 on 2025-07-05 11:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ieltstest', '0002_listeningtext_remove_question_reading_text_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wquestion_text', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='WritingText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wtitle', models.CharField(max_length=200)),
                ('writing_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wanswer_text', models.TextField()),
                ('wquestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wanswers', to='ieltstest.wquestion')),
            ],
        ),
        migrations.AddField(
            model_name='wquestion',
            name='writing_text',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wquestions', to='ieltstest.writingtext'),
        ),
    ]
