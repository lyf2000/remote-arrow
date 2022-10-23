from core.views import ControlPageView
from django.urls import path

urlpatterns = [
    path("", ControlPageView.as_view(), name="home"),
    path("<slug:slug>", ControlPageView.as_view(), name="home"),
]
