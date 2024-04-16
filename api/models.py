from django.db import models
from django.utils import timezone
class Customer(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    mail = models.EmailField()
    location = models.CharField(max_length=100)
    industry = models.CharField(max_length=100,null=True)
    about = models.TextField()
    review = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    photo = models.ImageField(upload_to='customer_photos/', null=True, blank=True)
    photo_url = models.TextField(null=True, blank=True)
    problem = models.TextField(null=True, blank=True,default='no content')
    solution = models.TextField(null=True, blank=True,default='no content')
    output1=models.CharField(max_length=100,null=True, blank=True,default='no content')
    output1_text=models.TextField(null=True, blank=True,default='no content')
    output2=models.CharField(max_length=100,null=True, blank=True,default='no content')
    output2_text=models.TextField(null=True, blank=True,default='no content')
    output3=models.CharField(max_length=100,null=True, blank=True,default='no content')
    output3_text=models.TextField(null=True, blank=True,default='no content')

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        # Set filename based on company name if photo is provided
        if self.photo:
            filename = f"company_{self.id}.{self.photo.name.split('.')[1]}"
            self.photo.name = filename
            self.photo_url = self.photo.url  # Set photo URL
        super().save(*args, **kwargs)



class Testinominal(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    photo = models.ImageField(upload_to='customer_photos/', null=True, blank=True)
    photo_url = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        # Set filename based on company name if photo is provided
        if self.photo:
            filename = f"{self.id}.{self.photo.name.split('.')[1]}"
            self.photo.name = filename
            self.photo_url = self.photo.url  # Set photo URL
        super().save(*args, **kwargs)


class Query(models.Model):
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    mobile = models.CharField(max_length=10,null=True)
    message=models.TextField(null=True)
    date=models.DateTimeField(null=True,default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    
    