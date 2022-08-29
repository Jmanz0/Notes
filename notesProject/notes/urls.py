from django.urls import path, include
from .views import *

urlpatterns = [
    path("", home_view, name = 'note-list'),
    path("create/", create_view, name = 'note-create'),
    path("filter/", filter_view, name = 'note-filter'),
    path("login/", login_page_view, name = 'note-login'),
    path("logout/", logout_user, name = 'note-logout'),
    path("register/", register_user, name = 'note-register'),
    path("<int:id>/delete/", delete_view, name = 'note-delete'),
    path("<int:id>/update/", update_view, name = 'note-update')
]