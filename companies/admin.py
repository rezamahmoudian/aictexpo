from django.contrib import admin
from.models import Company, CompanyCategory, Product, ProductCategory


# Register your models here.
class AdminCompany(admin.ModelAdmin):
    list_display = ('name', 'manager', 'website', 'email', 'mobile')
    # list_filter = ('publish', 'status', 'author')
    # ordering = ('-status', '-publish')
    search_fields = ('name', 'about', 'manager')
    prepopulated_fields = {'slug': ('name', )}
    # actions = [make_publish, make_draft]


class AdminCompanyCategory(admin.ModelAdmin):
    list_display = ('title', )
    prepopulated_fields = {'slug': ('title',)}


class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'author', 'company')
    search_fields = ('title', 'short_description', 'author')
    prepopulated_fields = {'slug': ('title', )}
    # actions = [make_publish, make_draft]


class AdminProductCategory(admin.ModelAdmin):
    list_display = ('title', )
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Company, AdminCompany)
admin.site.register(CompanyCategory, AdminCompanyCategory)
admin.site.register(Product, AdminProduct)
admin.site.register(ProductCategory, AdminProductCategory)

