from django.urls import path
from . import views

urlpatterns = [
    path("", views.study_group_list, name="study_group_list"),
    path("group/<int:group_id>/", views.study_group_detail, name="study_group_detail"),
    path("group/<int:group_id>/register/", views.register_to_group, name="register_to_group"),
    path("group/<int:group_id>/cancel/", views.cancel_registration, name="cancel_registration"),
    path("my-registrations/", views.my_registrations, name="my_registrations"),
    path("my-groups/", views.organizer_dashboard, name="organizer_dashboard"),
    path("group/create/", views.create_study_group, name="create_study_group"),
    path("group/<int:group_id>/edit/", views.edit_study_group, name="edit_study_group"),
    path("group/<int:group_id>/delete/", views.delete_study_group, name="delete_study_group"),
    path("group/<int:group_id>/attendees/", views.group_attendees, name="group_attendees"),
]
