from django.db import models
from django.utils import timezone
from datetime import timedelta


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название товара")
    category = models.CharField(max_length=255, verbose_name="Категория")
    is_active = models.BooleanField(default=True, verbose_name="Статус активности")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return self.name

    def orders_previous_month(self):
        """Подсчитывает общее количество заказов за прошлый месяц"""
        today = timezone.now().date()
        first_day_current = today.replace(day=1)
        last_day_previous = first_day_current - timedelta(days=1)
        first_day_previous = last_day_previous.replace(day=1)
        orders = self.order_set.filter(
            order_date__gte=first_day_previous, order_date__lte=last_day_previous
        )
        total = orders.aggregate(total=models.Sum("quantity"))["total"]
        return total or 0

    def orders_current_month(self):
        """Подсчитывает общее количество заказов за текущий месяц, начиная с 1 числа"""
        today = timezone.now().date()
        first_day_current = today.replace(day=1)
        orders = self.order_set.filter(order_date__gte=first_day_current)
        total = orders.aggregate(total=models.Sum("quantity"))["total"]
        return total or 0


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date = models.DateField(verbose_name="Дата заказа", default=timezone.now)
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")

    def __str__(self):
        return f"Заказ товара {self.product.name} от {self.order_date}"
