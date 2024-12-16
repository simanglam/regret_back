# Generated by Django 5.1.4 on 2024-12-16 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('sold', models.BooleanField(default=False)),
                ('img', models.FileField(default='images/None/no-img.jpg', upload_to='images/')),
            ],
        ),
    ]