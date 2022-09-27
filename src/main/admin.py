from django.contrib import admin

from .models import Product, Cart, Order

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'price', 'model', 'asin')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
  list_display = ('id', 'user')

  readonly_fields = ['id', 'user', 'get_orders']
  fieldsets = [
    ('Cart Info', {'fields': ['id', 'user']}),
    ('Orders', {'fields': ['get_orders']})
  ]

  @admin.display(description="Orders")
  def get_orders(self, obj):
    return obj.order_set.all()


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
  list_display = ('id', 'product', 'cart', 'price', 'created_date')