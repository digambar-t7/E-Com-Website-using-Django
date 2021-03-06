# Generated by Django 3.2.6 on 2021-10-29 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPosts',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('head1', models.CharField(max_length=100)),
                ('desc1', models.CharField(max_length=5000)),
                ('head2', models.CharField(max_length=100)),
                ('desc2', models.CharField(max_length=5000)),
                ('head3', models.CharField(max_length=100)),
                ('desc3', models.CharField(max_length=5000)),
                ('thumbnail', models.ImageField(default='', upload_to='blog/images')),
            ],
        ),
        migrations.DeleteModel(
            name='Viewer',
        ),
    ]
