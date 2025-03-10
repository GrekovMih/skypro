from django.contrib import admin
from .models import Product, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "category",
        "is_active",
        "price",
        "orders_previous_month",
        "orders_current_month",
    )
    search_fields = ("name", "category")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "order_date", "quantity")
