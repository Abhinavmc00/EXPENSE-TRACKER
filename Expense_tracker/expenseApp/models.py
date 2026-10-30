from django.db import models
from django.contrib.auth.models  import User

# Create your models here.

class Expense(models.Model):

    CATEGORY_CHOICES=(
        ("Food","Food"),
        ("Bill","Bill"),
        ("Fuel","Fuel")
    )

    PAYEMENT_CHOICES=(
        ("UPI","UPI"),
        ("Card","Card")
    )

    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=8,decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)
    category=models.CharField(max_length=100,choices=CATEGORY_CHOICES,default="Food")
    payment=models.CharField(max_length=20,choices=PAYEMENT_CHOICES,default="UPI")


    def __str__(self):
        return f"{self.title} - {self.amount}"

    