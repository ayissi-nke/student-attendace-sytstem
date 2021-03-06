# Generated by Django 2.2.3 on 2019-07-22 08:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('course_code', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('matricule', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('level', models.IntegerField()),
                ('user', models.ForeignKey(on_delete='models.CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete='models.CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.ForeignKey(on_delete='models.CASCADE', to='account.Courses')),
                ('st_mtrl', models.ForeignKey(on_delete='models.CASCADE', to='account.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('date', models.DateField(auto_now_add=True)),
                ('course_code', models.ForeignKey(null=True, on_delete='models.CASCADE', to='account.Courses')),
                ('st_mtrl', models.ForeignKey(on_delete='models.CASCADE', to='account.Student')),
            ],
        ),
        migrations.AddField(
            model_name='courses',
            name='teachers',
            field=models.ForeignKey(on_delete='models.CASCADE', to='account.Teachers'),
        ),
    ]
