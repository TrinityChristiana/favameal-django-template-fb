from django.db import models


class FavoriteRestaurant(models.Model):
    """Favorite Restaurant model
        Join model for the many to many relationship between user and restaurant
    """
    user_id = models.CharField(max_length=255)
    restaurant = models.ForeignKey(
        "Restaurant", on_delete=models.CASCADE, related_name="userfavoriterestaurants")
