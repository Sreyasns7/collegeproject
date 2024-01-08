# Generated by Django 5.0 on 2024-01-04 10:40

import django.db.models.deletion
import django.db.models.expressions
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255)),
                ('fee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=255)),
                ('student_address', models.CharField(max_length=255)),
                ('student_age', models.IntegerField(blank=True, default=1, null=True)),
                ('joining_date', models.DateField()),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collegeapp.course')),
            ],
        ),
        migrations.CreateModel(
            name='Usermember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('number', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.expressions.Case, to='collegeapp.course')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.expressions.Case, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
