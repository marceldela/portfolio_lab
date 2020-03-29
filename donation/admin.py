from django.contrib import admin

from donation.models import Institution, Category, Donation


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    pass