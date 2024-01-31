from django.db import models

class Add_Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    additionalField1 = models.CharField(max_length=100)
    additionalField2 = models.CharField(max_length=100)
    additionalField3 = models.CharField(max_length=100)
    additionalField4 = models.CharField(max_length=100)
    additionalField5 = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name


class Ordered_Product(models.Model):
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    size = models.CharField(max_length=50)
    price = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_name} - {self.quantity} - {self.size} - {self.price} - {self.date}"
    


# class UserProfile(models.Model):
#     user_name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     height = models.DecimalField(max_digits=5, decimal_places=2)
#     weight = models.DecimalField(max_digits=5, decimal_places=2)
#     any_disease = models.CharField(max_length=100, blank=True, null=True)
#     allergies = models.CharField(max_length=100, blank=True, null=True)

#     def __str__(self):
#         return self.user_name
    



