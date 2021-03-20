from django.contrib import admin
from .models import Book
from import_export.admin import ImportExportModelAdmin, ImportExportMixin, ImportExportActionModelAdmin

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_filter = ['id', 'name', 'line', 'type']