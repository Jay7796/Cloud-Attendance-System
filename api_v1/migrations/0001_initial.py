# Generated by Django 2.1.5 on 2020-09-13 06:39

import api_v1.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recordAdded', models.DateTimeField(auto_now_add=True)),
                ('recordModified', models.DateTimeField(auto_now=True)),
                ('lectureDate', models.DateTimeField()),
                ('status', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('recordAdded', models.DateTimeField(auto_now_add=True)),
                ('recordModified', models.DateTimeField(auto_now=True)),
                ('studentId', models.UUIDField(default=api_v1.models.generateUUID, editable=False, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('mobileNo', models.CharField(max_length=15)),
                ('department', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='studentSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recordAdded', models.DateTimeField(auto_now_add=True)),
                ('recordModified', models.DateTimeField(auto_now=True)),
                ('studentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v1.student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='subjects',
            fields=[
                ('recordAdded', models.DateTimeField(auto_now_add=True)),
                ('recordModified', models.DateTimeField(auto_now=True)),
                ('subjectCode', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v1.student', to_field='department')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='studentsubject',
            name='subjectCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v1.subjects'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='studentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v1.student'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='subjectCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v1.subjects'),
        ),
    ]
