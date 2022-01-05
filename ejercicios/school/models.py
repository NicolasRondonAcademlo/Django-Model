from django.db import models


# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Subject(models.Model):
    title = models.CharField(max_length=20)
    duration = models.DurationField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Student(models.Model):
    GENDER_CHOICES = (
        ("m", "Hombre"),
        ("f", "Mujer")
    )
    first_name = models.CharField(max_length=30,
                                  null=False
                                  )
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    is_repeated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return self.first_name
