# Generated by Django 3.0.3 on 2020-04-23 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200423_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default='KZ87CJ', max_length=6, primary_key=True, serialize=False),
        ),
    ]