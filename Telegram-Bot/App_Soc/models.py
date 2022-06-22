from datetime import datetime, timedelta
from django.db import models
from django.utils import timezone


class Question(models.Model):
    name_text = models.CharField(max_length=200)
    ic_text = models.CharField(max_length=200, primary_key=True)
    phone_text = models.CharField(max_length=200)
    income = models.IntegerField(verbose_name='Income')
    address1 = models.CharField(max_length=100, verbose_name='Alamat 1')
    address2 = models.CharField(max_length=100, verbose_name='Alamat 2')
    city = models.CharField(max_length=20, verbose_name='Bandar')
    mukim = models.CharField(max_length=20, verbose_name='Mukim')
    parlimen = models.CharField(max_length=20, verbose_name='Parlimen')
    state = models.CharField(max_length=20, verbose_name='Negeri')
    poskod = models.IntegerField(verbose_name='Poskod')
    pub_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.ic_text}, {self.name_text}, {self.income}"
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def calculate_age(self):
        birthday = self.ic_text[:6]
        date_time_obj = datetime.strptime(birthday, '%y%m%d')
        if date_time_obj > datetime.now():
            date_time_obj -= timedelta(weeks=5124, days=2)
        age = datetime.now() - date_time_obj
        ageYears = int(age.days / 365)
        return ageYears

class Post(models.Model):
    name = models.CharField(max_length=200, unique=True)
    ic = models.CharField(max_length=200, primary_key=True)
    phone = models.CharField(max_length=200)
    dateregister = models.DateTimeField('%Y-%m-%d')
    def calculate_age(self):
        birthday = self.ic[:6]
        date_time_obj = datetime.strptime(birthday, '%y%m%d')
        if date_time_obj > datetime.now():
            date_time_obj -= timedelta(weeks=5124, days=2)
        age = datetime.now() - date_time_obj
        ageYears = int(age.days / 365)
        return ageYears