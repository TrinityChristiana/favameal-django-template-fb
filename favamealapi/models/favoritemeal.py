from django.db import models


class FavoriteMeal(models.Model):
    """Favorite Meal model
        Join model for the many to many relationship between user and meal
    """
    user_id =models.CharField(max_length=255)
    meal = models.ForeignKey(
        "Meal", on_delete=models.CASCADE, related_name="userfavoritemeals")
