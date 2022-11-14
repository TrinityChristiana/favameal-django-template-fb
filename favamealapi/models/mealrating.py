from django.db import models


class MealRating(models.Model):
    """Meal Rating model
    Holds the rating a user has given a meal
    """
    user_id = models.CharField(max_length=255)
    meal = models.ForeignKey(
        "Meal", on_delete=models.CASCADE, related_name="mealrating")
    rating = models.IntegerField()
