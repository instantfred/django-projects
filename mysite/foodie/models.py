from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):

    def __str__(self):
        """
        Returns a string representation of the model instance.

        This method is used to define how the model instance should be represented
        as a string. It is commonly used in Django admin and shell to display
        meaningful information about the object.

        Returns:
            str: The name of the item.
        """
        # This method is used to provide a human-readable representation of the object.
        return self.item_name
    

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=100)
    item_description = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://metropizza.com.au/wp-content/uploads/2023/06/food-placeholder.jpeg")