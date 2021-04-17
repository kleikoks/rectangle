from django.contrib import admin
from .models import Book
from adminsortable2.admin import SortableAdminMixin


@admin.register(Book)
class BookAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass