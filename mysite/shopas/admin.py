from django.contrib import admin
from .models import Category, Item, Order, Designer


class ItemOrderInline(admin.TabularInline):
    model = Order
    extra = 0
    can_delete = False


class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'designer', 'display_category')
    inlines = [ItemOrderInline]


class DesignerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'display_items')


class ItemOrderAdmin(admin.ModelAdmin):
    list_display = ('item', 'status', 'client', 'due_date')
    search_fields = ('id', 'item_title')
    list_filter = ('item', 'status')
    list_editable = ('due_date', 'status', 'client')

    fieldsets = (
        ('General', {'fields': ('item', 'client')}),
        ('Availability', {'fields': ('status', 'due_date')}),
    )


admin.site.register(Category)
admin.site.register(Item, ItemAdmin)
admin.site.register(Order, ItemOrderAdmin)
admin.site.register(Designer, DesignerAdmin)