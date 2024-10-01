from django.urls import path
from django.views.generic import TemplateView
from .views import (
    ContactCreateView,
    MainView,
    Section3View1,
    Section3View2,
    Section3View3,
    Section3View4,
    Section3View5,
)

urlpatterns = [
    path("", MainView.as_view(), name="home"),
    path("sek3__1/", Section3View1.as_view(), name="sek3__1"),
    path("sek3__2/", Section3View2.as_view(), name="sek3__2"),
    path("sek3__3/", Section3View3.as_view(), name="sek3__3"),
    path("sek3__4/", Section3View4.as_view(), name="sek3__4"),
    path("sek3__5/", Section3View5.as_view(), name="sek3__5"),
    path("submit/", ContactCreateView.as_view(), name="submit"),
    path(
        "success/", TemplateView.as_view(template_name="success.html"), name="success"
    ),
]
