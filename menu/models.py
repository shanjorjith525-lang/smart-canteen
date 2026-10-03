from django.db import models
from django.contrib.auth.models import User


# =========================
# FOOD
# =========================

class Food(models.Model):

    name = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    available_quantity = models.PositiveIntegerField(
        default=0
    )

    is_available = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name


# =========================
# ORDER
# =========================

class Order(models.Model):

    STATUS_CHOICES = [

        ('pending', 'Pending'),

        ('preparing', 'Preparing'),

        ('ready', 'Ready'),

        ('completed', 'Completed'),

    ]

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField()

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    ordered_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.food.name} x {self.quantity}"


# =========================
# FOOD WASTE
# =========================

class FoodWaste(models.Model):

    REASON_CHOICES = [

        ('leftover', 'Leftover Food'),

        ('expired', 'Expired'),

        ('damaged', 'Damaged'),

        ('overcooked', 'Overcooked'),

        ('spilled', 'Spilled'),

        ('other', 'Other'),

    ]

    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField()

    reason = models.CharField(
        max_length=30,
        choices=REASON_CHOICES
    )

    date = models.DateField(
        auto_now_add=True
    )

    notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return (
            f"{self.food.name} - "
            f"{self.quantity} waste"
        )