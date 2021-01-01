from django.contrib import admin


from .models import Stock, Category
from .forms import StockCreateForm


# Register your models here.


class StockCreateAdmin(admin.ModelAdmin):
    list_display = ['category', 'game_title', 'quantity', 'manufacturer', 'price']
    form = StockCreateForm
    list_filter = ['category']
    search_fields = ['category', 'game_title']

admin.site.register(Stock, StockCreateAdmin)
admin.site.register(Category)