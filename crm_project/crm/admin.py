from django.contrib import admin

from .models import Customer, Product, Employee, Task


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')
    list_filter = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)
    list_filter = ('name','price')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'hired_date')
    search_fields = ('user__username', 'position')
    list_filter = ('hired_date','position')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'assigned_to')
    search_fields = ('title', 'description')
    list_filter = ('status','assigned_to')  # Add a comma to make it a tuple
