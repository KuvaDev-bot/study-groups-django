from django.contrib import admin
from .models import Registration, StudyGroup

class RegistrationInline(admin.TabularInline):
    model = Registration
    extra = 0
    readonly_fields = ("registered_at",)


@admin.register(StudyGroup)
class StudyGroupAdmin(admin.ModelAdmin):
    list_display = (
        "subject",
        "scheduled_at",
        "location",
        "max_participants",
        "participant_total",
        "organizer",
    )
    list_filter = ("scheduled_at",)
    search_fields = ("subject", "description", "location")
    inlines = [RegistrationInline]

    @admin.display(description="Iscritti")
    def participant_total(self, obj):
        return obj.participant_count


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("attendee", "study_group", "registered_at")
    list_filter = ("registered_at",)
    search_fields = ("attendee__username", "study_group__subject")

