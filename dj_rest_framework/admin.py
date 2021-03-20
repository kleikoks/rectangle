from django.contrib import admin
from .models import WasteUtil, WasteUtilCategory, WasteUtilReview
# Register your models here.

@admin.register(WasteUtil)
class WasteUtilAdmin(admin.ModelAdmin):
    pass

@admin.register(WasteUtilCategory)
class WasteUtilCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(WasteUtilReview)
class WasteUtilReviewAdmin(admin.ModelAdmin):
    pass