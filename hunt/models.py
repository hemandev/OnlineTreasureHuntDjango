from django.db import models

# Create your models here.


class UserModel(models.Model):

    name = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    uid = models.CharField(max_length=100,unique=True)
    phone = models.IntegerField()
    date_joined = models.DateTimeField(auto_now=True)
    super_user = models.BooleanField(default=False)
    email = models.EmailField(default='admin@gmail.com')
    level = models.IntegerField(default=1)

    def __str__(self):
        return self.name + " " + self.uid


class LevelModel(models.Model):
    level_no = models.IntegerField()
    question_text = models.TextField()
    question_image = models.FileField(upload_to='levels/')
    answer = models.CharField(max_length=100)
    placeholder_ans = models.CharField(max_length=100, default='Answer')
    title = models.CharField(max_length=100)

    def __str__(self):
        return "Level" + str(self.level_no) + " " + self.answer


