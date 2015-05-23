# coding: utf8
from django.db import models
from django.contrib.auth.models import User


class StepUsers(models.Model):
    stepUser = models.ForeignKey(User, verbose_name='Пользователь')
    age = models.IntegerField('Возраст')
    city = models.CharField('Город', max_length=50)
    photo = models.ImageField('Фото', upload_to='users/photo')
    steps = models.BigIntegerField('Общее количество шагов')

    def __unicode__(self):
        return unicode(self.stepUser)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class StepUsersHistory(models.Model):
    user = models.ForeignKey(StepUsers, verbose_name='Пользователь')
    date = models.DateField('Дата', auto_now_add=True)
    steps = models.BigIntegerField('Количество шагов')

    def __unicode__(self):
        return unicode(self.user)

    class Meta:
        verbose_name = 'история пользователя'
        verbose_name_plural = 'истории пользователя'