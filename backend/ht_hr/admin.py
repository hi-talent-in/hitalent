from django.contrib import admin

from .models import Intern


class InternAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "address",
    ]
    list_display_links = ["email", "first_name"]


admin.site.register(Intern, InternAdmin)
