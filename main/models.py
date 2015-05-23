# coding: utf8
from django.db import models
from django.contrib.auth.models import User


class StepUsers(models.Model):
    stepUser = models.ForeignKey(User, verbose_name='Пользователь')
    # username = models.CharField('Логин', max_length=50)
    # password = models.CharField('Пароль', max_length=20)
    # firstname = models.CharField('Имя', max_length=50)
    # lastname = models.CharField('Фамилия', max_length=50)
    age = models.IntegerField('Возраст')
    # growth = models.IntegerField('Рост')
    # weight = models.IntegerField('Вес')
    city = models.CharField('Город', max_length=50)
    photo = models.ImageField('Фото', upload_to='users/photo')

    def __unicode__(self):
        return unicode(self.user)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class StepUsersHistory(models.Model):
    user = models.ForeignKey(StepUsers, verbose_name='Пользователь')
    date = models.DateField('Дата', auto_now=True)
    steps = models.BigIntegerField('Количество шагов')

    def __unicode__(self):
        return unicode(self.user)

    class Meta:
        verbose_name = 'история пользователя'
        verbose_name_plural = 'истории пользователя'