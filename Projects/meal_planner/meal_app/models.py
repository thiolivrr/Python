from django.db import models

class Meal(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text
    
class Description(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'descriptions'
    def __str__(self):
        return f"{self.text[:50]}..."
