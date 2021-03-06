# Generated by Django 3.2.8 on 2021-11-15 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=200)),
                ('ic_text', models.CharField(max_length=200)),
                ('phone_text', models.CharField(max_length=200)),
                ('income', models.IntegerField(verbose_name='Poskod')),
                ('address1', models.CharField(max_length=100, verbose_name='Alamat 1')),
                ('address2', models.CharField(max_length=100, verbose_name='Alamat 2')),
                ('city', models.CharField(max_length=20, verbose_name='Bandar')),
                ('mukim', models.CharField(max_length=20, verbose_name='Mukim')),
                ('parlimen', models.CharField(max_length=20, verbose_name='Parlimen')),
                ('state', models.CharField(max_length=20, verbose_name='Negeri')),
                ('poskod', models.IntegerField(verbose_name='Poskod')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
