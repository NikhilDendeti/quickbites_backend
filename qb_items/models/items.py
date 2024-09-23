from django.db import models
import uuid

class Category(models.Model):
    name=models.CharField(max_length=150)
    category_id=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)

    def __str__(self):
         return self.name

class FoodItem(models.Model):
     item_id=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
     name=models.CharField(max_length=150)
     category=models.ForeignKey(Category,on_delete=models.CASCADE)
     price=models.DecimalField(max_digits=10,decimal_places=2)
     description=models.TextField()
     item_image_url=models.URLField()
     is_veg=models.BooleanField()

     def __str__(self):
         return self.name

