from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField()
    grade = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} (Roll No: {self.roll_number})"
