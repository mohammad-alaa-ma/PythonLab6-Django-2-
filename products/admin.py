from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'price', 'in_stock', 'created_at')
    list_filter = ('created_at', 'in_stock')
    search_fields = ('name', 'code', 'description')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('price', 'in_stock')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'code', 'description')
        }),
        ('Pricing & Stock', {
            'fields': ('price', 'in_stock')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
