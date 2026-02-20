from django.db import models
from django.conf import settings
from restaurants.models import Restaurant

User = settings.AUTH_USER_MODEL

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    reserved_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.restaurant}"


class Visit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    visited_at = models.DateField()
    memo = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user} visited {self.restaurant}"