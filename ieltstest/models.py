from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Profile
class TestScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100)
    score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.test_name} - {self.score}"


# User Answer Model
class UserAnswer(models.Model):
    test_score = models.ForeignKey(TestScore, on_delete=models.CASCADE, related_name='user_answers')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    question = GenericForeignKey('content_type', 'object_id')
    user_answer = models.TextField()    
    is_correct = models.BooleanField()     

    def __str__(self):
        return f"Answer by {self.test_score.user.username} for {self.test_score.test_name}"


# Reading Test Part
class ReadingText(models.Model):
    rtitle = models.CharField(max_length=200)
    rimage = models.ImageField(upload_to='reading_images/')

    def __str__(self):
        return self.rtitle

class RQuestion(models.Model):
    reading_text = models.ForeignKey(ReadingText, on_delete=models.CASCADE, related_name='rquestions')
    rquestion_text = models.CharField(max_length=300)

    def __str__(self):
        return self.rquestion_text

class RAnswer(models.Model):
    rquestion = models.ForeignKey(RQuestion, on_delete=models.CASCADE, related_name='ranswers')
    ranswer_text = models.CharField(max_length=200)
    is_correct_for_reading = models.BooleanField(default=False)

    def __str__(self):
        return self.ranswer_text

# Listening Test Part
class ListeningText(models.Model):
    ltitle = models.CharField(max_length=200)
    laudio_file = models.FileField(upload_to='listening_audio/')

    def __str__(self):
        return self.ltitle

class LQuestion(models.Model):
    listening_text = models.ForeignKey(ListeningText, on_delete=models.CASCADE, related_name='lquestions')
    lquestion_text = models.CharField(max_length=300)

    def __str__(self):
        return self.lquestion_text

class LAnswer(models.Model):
    lquestion = models.ForeignKey(LQuestion, on_delete=models.CASCADE, related_name='lanswers')
    lanswer_text = models.CharField(max_length=200)
    is_correct_for_listening = models.BooleanField(default=False)

    def __str__(self):
        return self.lanswer_text

# Writing Test Part
class WritingText(models.Model):
    TASK_CHOICES = [
        ('task1', 'Task 1'),
        ('task2', 'Task 2'),
    ]
    writing_image = models.ImageField(upload_to='writing_images/', null=True)  # Only image upload
    task_type = models.CharField(max_length=5, choices=TASK_CHOICES, null=True)  # Specify task type

    def __str__(self):
        return f"{self.get_task_type_display()}"  # Display task type


class WQuestion(models.Model):
    writing_text = models.ForeignKey(WritingText, on_delete=models.CASCADE, related_name='wquestions')
    wquestion_text = models.CharField(max_length=300)

    def __str__(self):
        return self.wquestion_text

class WAnswer(models.Model):
    wquestion = models.ForeignKey(WQuestion, on_delete=models.CASCADE, related_name='wanswers')
    wanswer_text = models.TextField()

    def __str__(self):
        return self.wanswer_text
    
# Contact
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
# Universities List 
class UniversityList(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    world_ranking = models.IntegerField(null=True)
    logo = models.ImageField(upload_to='university_logos/')
    ielts_score_required = models.FloatField()

    def __str__(self):
        return self.name