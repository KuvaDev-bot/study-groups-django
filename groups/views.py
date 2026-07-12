from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Registration, StudyGroup
from .forms import StudyGroupForm


def study_group_list(request):
    study_groups = StudyGroup.objects.all()

    return render(
        request,
        "groups/study_group_list.html",
        {"study_groups": study_groups},
    )


def study_group_detail(request, group_id):
    study_group = get_object_or_404(StudyGroup, id=group_id)

    is_registered = False
    if request.user.is_authenticated:
        is_registered = Registration.objects.filter(
            study_group=study_group,
            attendee=request.user,
        ).exists()
        
    return render(
        request,
        "groups/study_group_detail.html",
        {
            "study_group": study_group,
            "is_registered": is_registered,
        },
    )


@login_required
def register_to_group(request, group_id):
    study_group = get_object_or_404(StudyGroup, id=group_id)

    if request.method != "POST":
        return redirect("study_group_detail", group_id=study_group.id)

    if request.user.role != "ATTENDEE":
        messages.error(request, "Solo gli attendee possono iscriversi ai gruppi.")
        return redirect("study_group_detail", group_id=study_group.id)

    if study_group.is_full:
        messages.error(request, "Non puoi iscriverti: il gruppo è completo.")
        return redirect("study_group_detail", group_id=study_group.id)

    already_registered = Registration.objects.filter(
        study_group=study_group,
        attendee=request.user,
    ).exists()

    if already_registered:
        messages.error(request, "Sei già iscritto a questo gruppo.")
        return redirect("study_group_detail", group_id=study_group.id)

    Registration.objects.create(study_group=study_group, attendee=request.user)
    messages.success(request, "Iscrizione completata con successo.")
    return redirect("study_group_detail", group_id=study_group.id)


@login_required
def cancel_registration(request, group_id):
    study_group = get_object_or_404(StudyGroup, id=group_id)

    if request.method != "POST":
        return redirect("study_group_detail", group_id=study_group.id)

    registration = Registration.objects.filter(
        study_group=study_group,
        attendee=request.user,
    ).first()

    if registration is None:
        messages.error(request, "Non risulti iscritto a questo gruppo.")
        return redirect("study_group_detail", group_id=study_group.id)

    registration.delete()
    messages.success(request, "Iscrizione annullata.")
    return redirect("study_group_detail", group_id=study_group.id)


@login_required
def my_registrations(request):
    registrations = Registration.objects.filter(attendee=request.user)
    return render(request, "groups/my_registrations.html", {"registrations": registrations})

@login_required
def organizer_dashboard(request):
    if request.user.role != "ORGANIZER":
        messages.error(request, "Questa pagina è riservata agli organizer.")
        return redirect("study_group_list")

    study_groups = StudyGroup.objects.filter(organizer=request.user)

    return render(
        request,
        "groups/organizer_dashboard.html",
        {"study_groups": study_groups},
    )


@login_required
def create_study_group(request):
    if request.user.role != "ORGANIZER":
        messages.error(request, "Solo gli organizer possono creare gruppi.")
        return redirect("study_group_list")

    if request.method == "POST":
        form = StudyGroupForm(request.POST)

        if form.is_valid():
            study_group = form.save(commit=False)
            study_group.organizer = request.user
            study_group.save()

            messages.success(request, "Gruppo di studio creato.")
            return redirect("organizer_dashboard")
    else:
        form = StudyGroupForm()

    return render(
        request,
        "groups/study_group_form.html",
        {
            "form": form,
            "title": "Crea un gruppo di studio",
        },
    )


@login_required
def edit_study_group(request, group_id):
    study_group = get_object_or_404(StudyGroup, id=group_id)

    if request.user != study_group.organizer:
        messages.error(request, "Non puoi modificare questo gruppo.")
        return redirect("study_group_detail", group_id=study_group.id)

    if request.method == "POST":
        form = StudyGroupForm(request.POST, instance=study_group)

        if form.is_valid():
            form.save()

            messages.success(request, "Gruppo modificato correttamente.")
            return redirect("organizer_dashboard")
    else:
        form = StudyGroupForm(instance=study_group)

    return render(
        request,
        "groups/study_group_form.html",
        {
            "form": form,
            "title": "Modifica gruppo di studio",
        },
    )


@login_required
def delete_study_group(request, group_id):
    study_group = get_object_or_404(StudyGroup, id=group_id)

    if request.user != study_group.organizer:
        messages.error(request, "Non puoi eliminare questo gruppo.")
        return redirect("study_group_detail", group_id=study_group.id)

    if request.method == "POST":
        study_group.delete()

        messages.success(request, "Gruppo eliminato.")
        return redirect("organizer_dashboard")

    return render(
        request,
        "groups/delete_study_group.html",
        {"study_group": study_group},
    )


@login_required
def group_attendees(request, group_id):
    study_group = get_object_or_404(StudyGroup, id=group_id)

    if request.user != study_group.organizer:
        messages.error(request, "Non puoi vedere gli iscritti di questo gruppo.")
        return redirect("study_group_detail", group_id=study_group.id)

    registrations = Registration.objects.filter(study_group=study_group)

    return render(
        request,
        "groups/group_attendees.html",
        {
            "study_group": study_group,
            "registrations": registrations,
        },
    )