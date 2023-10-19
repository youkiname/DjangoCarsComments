from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, related_name='brands', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.country.name}"


class Car(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, related_name='cars', on_delete=models.CASCADE)
    release_year = models.IntegerField()
    release_end_year = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.release_year}"


class Comment(models.Model):
    email = models.CharField()
    car = models.ForeignKey(Car, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.text
