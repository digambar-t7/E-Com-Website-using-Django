# create a class here with all the parameters needed 
# then register this class in admin.py
# it will create required tables in the default db.sqlite3 file

from django.db import models

# Create your models here.
class BlogPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    head1 = models.CharField(max_length=100)
    desc1 = models.CharField(max_length=5000)
    head2 = models.CharField(max_length=100)
    desc2 = models.CharField(max_length=5000)
    head3 = models.CharField(max_length=100)
    desc3 = models.CharField(max_length=5000)
    thumbnail = models.ImageField(upload_to='blog/images',default='')

    def __str__(self):
        return self.title