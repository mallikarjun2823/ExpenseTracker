from django.core.management.base import BaseCommand
from expenses.models import User, Expense
from datetime import date

class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **options):
        # Clear existing data
        Expense.objects.all().delete()
        User.objects.all().delete()

        # Create sample users
        user1 = User.objects.create(
            user_name='John Doe',
            email='john@example.com',
            password='hashedpassword1'  # In real app, use proper hashing
        )
        user2 = User.objects.create(
            user_name='Jane Smith',
            email='jane@example.com',
            password='hashedpassword2'
        )

        # Create sample expenses
        Expense.objects.create(
            user=user1,
            amount=50.00,
            description='Lunch at restaurant',
            expense_date=date.today(),
            category='Food'
        )
        Expense.objects.create(
            user=user1,
            amount=25.00,
            description='Coffee',
            expense_date=date.today(),
            category='Food'
        )
        Expense.objects.create(
            user=user2,
            amount=100.00,
            description='Gas',
            expense_date=date.today(),
            category='Transportation'
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with sample data'))