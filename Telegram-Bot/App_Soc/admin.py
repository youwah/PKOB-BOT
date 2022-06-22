from django.contrib import admin

from .models import Question

#admin.site.register(Question)

@admin.register(Question)
class PersonAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('name_text', 'ic_text', 'income', 'address1', 'address2', 'city', 'mukim', 'parlimen', 'state', 'poskod', 'pub_date')
        return self.readonly_fields
    pass
