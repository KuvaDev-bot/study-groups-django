from django import forms
from .models import StudyGroup

class StudyGroupForm(forms.ModelForm):
    class Meta:
        model = StudyGroup
        fields = [
            "subject",
            "description",
            "scheduled_at",
            "location",
            "max_participants",
        ]

        widgets = {
            "scheduled_at": forms.DateTimeInput(
                attrs={"type": "datetime-local"}
            ),
        }