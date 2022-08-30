from django.db import models

# Create your models here.

class Poll(models.Model):
    question_no = models.IntegerField()
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=400)
    option2 = models.CharField(max_length=400)
    option3 = models.CharField(max_length=400)
    option4 = models.CharField(max_length=400)
    current_user_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.question}"

class Count_total_poll(models.Model):
    current_user_name = models.CharField(max_length=200)
    total_polls = models.IntegerField()

    def __str__(self):
        return f"{self.current_user_name} {self.total_polls}"

class Poll_statistics(models.Model):
    username = models.CharField(max_length=200)
    question_no = models.IntegerField()
    answer1_count = models.IntegerField()
    answer2_count = models.IntegerField()
    answer3_count = models.IntegerField()
    answer4_count = models.IntegerField()
    total_answer = models.IntegerField()

    def __str__(self):
        return f"{self.username} {self.question_no}"
