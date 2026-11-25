from django.contrib import admin
from django.urls import include, path

from accounts import views as account_views
from notes import views as note_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", account_views.signup, name="signup"),
    path("profile/", account_views.profile, name="profile"),
    path("notes/new/", note_views.note_create, name="note_create"),
    path("", note_views.home, name="home"),
]
