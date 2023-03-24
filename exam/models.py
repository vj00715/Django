from django.db import models

# Create your models here.
class courses(models.Model):
    courseName = models.CharField(max_length=225)
    questionMarks = models.PositiveIntegerField()
    # totalQuestion = models.PositiveIntegerField()

    def __str__(self):
        return self.courseName

class Question(models.Model):
    course = models.ForeignKey(to = courses, on_delete = models.CASCADE)
    courseQuestion = models.CharField(max_length=225)
    id = models.AutoField(primary_key=True)
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    answer=models.CharField(max_length=200)

class result(models.Model):
    username = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    totalMarks = models.IntegerField(null=True)
    studentMarks = models.FloatField(null=True)