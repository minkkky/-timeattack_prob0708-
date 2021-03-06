# Generated by Django 4.0.6 on 2022-07-08 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_jobpost_salary'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.jobpost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_apply',
            },
        ),
    ]
