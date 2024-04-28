from django.db import models

# Create your models here.

class Review(models.Model):
    RATING_CHOICES=(
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    name=models.CharField(max_length=250, verbose_name='your_name')
    phone_number=models.IntegerField()
    message=models.TextField(max_length=500)
    published_date=models.DateField(auto_now_add=True)
    email=models.EmailField(null=False)
    rating=models.IntegerField(default=5, choices=RATING_CHOICES)

    
    def __str__(self) -> str:
        return self.name


class Contact_Us(models.Model):
    your_name=models.CharField(max_length=250)
    phone_number=models.IntegerField()
    your_message=models.TextField(max_length=500)
    published_date=models.DateField(auto_now_add=True)
    email=models.EmailField(null=False)


    def __str__(self) -> str:
        return self.name
