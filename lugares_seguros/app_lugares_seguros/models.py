from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Usar un campo protegido para contraseñas
    
    def __str__(self):
        return f"{self.name} {self.lastname}"

class Place(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    street = models.CharField(max_length=50)
    number = models.PositiveIntegerField(null=True)  # Permitimos que el número sea opcional
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    is_safe = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.street}, {self.number}, {self.city}, {self.state}, {self.country}"

class UserPlaceFeedback(models.Model):
    LIKE_CHOICES = (
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    feedback_type = models.CharField(max_length=7, choices=LIKE_CHOICES)

    class Meta:
        unique_together = ('user', 'place')  # Para evitar que un usuario pueda dar más de un like/dislike al mismo lugar

    def __str__(self):
        return f"{self.user.username} {self.feedback_type}d {self.place.street}"

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.place} at {self.created_at}"
