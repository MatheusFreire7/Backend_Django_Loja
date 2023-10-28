from django.urls import path
from api.views import root_views as views

urlpatterns = [
       path("", views.root_view, name="root"),
]
