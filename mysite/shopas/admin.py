from django.contrib import admin

# Register your models here.
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
    list_display = ('item', 'status')
    search_fields = ('unique_id', 'item_title')
    list_filter = ('item', 'status')

    fieldsets = (
        ('General', {'fields': ('unique_id', 'item')}),
        ('Availability', {'fields': ('status', 'due_back')}),
    )

    

admin.site.register(Category)
admin.site.register(Item, ItemAdmin)
admin.site.register(Order, ItemOrderAdmin)
admin.site.register(Designer, DesignerAdmin)