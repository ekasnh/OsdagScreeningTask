from django.db import models

class RectangularPrism(models.Model):
    designation = models.CharField(max_length=100, unique=True)
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()

    def __str__(self):
        return self.designation
