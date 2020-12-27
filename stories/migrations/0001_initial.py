# Generated by Django 3.1.4 on 2020-12-27 22:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=140, verbose_name='')),
                ('content', models.TextField(verbose_name='')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
