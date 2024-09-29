from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    investment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    risk_tolerance = models.CharField(max_length=100)

class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    risk_level = models.CharField(max_length=100)


class UserResponse(models.Model):
    invest_amount = models.DecimalField(max_digits=10, decimal_places=2)
    risk_level = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Investment Amount: {self.invest_amount}, Risk Level: {self.risk_level}"

