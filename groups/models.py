from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone


class StudyGroup(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField(
        help_text="Inserisci il programma o gli argomenti che saranno studiati."
    )
    scheduled_at = models.DateTimeField()
    location = models.CharField(
        max_length=150,
        help_text="Ad esempio: Centro didattico Morgagni, Biblioteca, Google Meet."
    )
    max_participants = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )
    organizer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="organized_study_groups",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["scheduled_at"]

    def __str__(self):
        return f"{self.subject} - {self.scheduled_at:%d/%m/%Y %H:%M}"

    @property
    def participant_count(self):
        return self.registrations.count()

    @property
    def is_full(self):
        return self.participant_count >= self.max_participants

    def clean(self):
        if self.scheduled_at and self.scheduled_at <= timezone.now():
            raise ValidationError(
                {"scheduled_at": "La data e l'ora del gruppo devono essere nel futuro."}
            )


class Registration(models.Model):
    study_group = models.ForeignKey(
        StudyGroup,
        on_delete=models.CASCADE,
        related_name="registrations",
    )
    attendee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="study_group_registrations",
    )
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["study_group", "attendee"],
                name="unique_study_group_registration",
            )
        ]
        ordering = ["-registered_at"]

    def __str__(self):
        return f"{self.attendee.username} - {self.study_group.subject}"

    def clean(self):
        if self.study_group_id and self.study_group.is_full:
            raise ValidationError(
                "Non è possibile iscriversi: il gruppo ha raggiunto il numero massimo di partecipanti."
            )