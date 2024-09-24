from django.db import models
import uuid


class Category(models.Model):
    name = models.CharField(max_length=150)
    category_id = models.UUIDField(primary_key=True, editable=False,
                                   default=uuid.uuid4)

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    item_id = models.UUIDField(primary_key=True, editable=False,
                               default=uuid.uuid4)
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    item_image_url = models.URLField()
    is_veg = models.BooleanField()

    def __str__(self):
        return self.name


class FoodItemsSelection(models.Model):
    selection_id = models.UUIDField(primary_key=True, editable=False,
                                    default=uuid.uuid4)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    selected_items_count = models.IntegerField(default=0)
    selection_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.selected_items_count} of {self.food_item.name} on {self.selection_date}'




