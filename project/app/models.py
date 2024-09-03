from django.db import models

# Create your models here.
class ItemInfo(models.Model):
    item_name=models.CharField(max_length=40)
    item_desc=models.CharField(max_length=30)
    item_price=models.IntegerField()
    item_image=models.ImageField(upload_to='image')
    itam_resume=models.FileField(upload_to='resume')
