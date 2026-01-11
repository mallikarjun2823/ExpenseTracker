from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'users'
        managed = False

    def __str__(self):
        return self.user_name

class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, null=True, blank=True)
    expense_date = models.DateField()
    category = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'expenses'
        managed = False

    def __str__(self):
        return f"{self.description} - {self.amount}"