from django.contrib import admin

from .models import Food, Order, FoodWaste


# =========================
# FOOD ADMIN
# =========================

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'price',
        'available_quantity',
        'is_available',
    )

    list_filter = (
        'is_available',
    )

    search_fields = (
        'name',
        'description',
    )


# =========================
# ORDER ADMIN
# =========================

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'food',
        'customer',
        'quantity',
        'total_price',
        'status',
        'ordered_at',
    )

    list_filter = (
        'status',
        'ordered_at',
    )

    search_fields = (
        'food__name',
        'customer__username',
    )

    ordering = (
        '-ordered_at',
    )


# =========================
# FOOD WASTE ADMIN
# =========================

@admin.register(FoodWaste)
class FoodWasteAdmin(admin.ModelAdmin):

    list_display = (
        'food',
        'quantity',
        'reason',
        'date',
        'created_at',
    )

    list_filter = (
        'reason',
        'date',
    )

    search_fields = (
        'food__name',
        'notes',
    )

    ordering = (
        '-date',
        '-created_at',
    )