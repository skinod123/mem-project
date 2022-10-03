from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Account(models.Model):
    username = models.CharField(verbose_name ='имя пользователя', max_length=255, unique=True, null=False)
    first_name = models.CharField(verbose_name ='первое имя',max_length=255)
    last_name = models.CharField(verbose_name ='последнее имя', max_length=255)
    age = models.SmallIntegerField(verbose_name ='возраст-лет', null=True)
    def __str__(self):
        return self.username

class Post(models.Model):
    title = models.CharField(verbose_name ='title', max_length=500)
    short_description = models.CharField(verbose_name ='вся инфа кратко', max_length=255)
    text = models.TextField(null=False)
    user_id = models.ForeignKey(Account, verbose_name='user_id', on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(Account,verbose_name='user', on_delete=models.CASCADE)
    text = models.TextField(verbose_name = 'text',null=False)
    pub_date = models.DateTimeField(verbose_name='date', auto_now_add=True)
    post_id = models.ForeignKey(Post, verbose_name='post',on_delete=models.CASCADE)
    def __str__(self):
        return self.text
