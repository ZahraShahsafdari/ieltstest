from django.db import models

from django.db import models

class ReadingText(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='reading_images/')

    def __str__(self):
        return self.title

class Question(models.Model):
    reading_text = models.ForeignKey(ReadingText, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=300)

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text