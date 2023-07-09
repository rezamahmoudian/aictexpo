from django.contrib import admin
from.models import Company, CompanyCategory


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


admin.site.register(Company, AdminCompany)
admin.site.register(CompanyCategory, AdminCompanyCategory)

