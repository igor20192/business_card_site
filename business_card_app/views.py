from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .models import (
    Contact,
    Footer,
    Gallery1,
    Gallery2,
    Gallery3,
    Gallery4,
    Gallery5,
    BiographyEvent,
)


class MainView(TemplateView):
    template_name = "html/main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        footer = Footer.objects.first()  # Получаем первую запись футера
        if footer:
            context["div_text"] = footer.div_text
            context["p1_text"] = footer.p1_text
            context["p2_text"] = footer.p2_text
            context["p3_text"] = footer.p3_text
        else:
            context["div_text"] = ""
            context["p1_text"] = ""
            context["p2_text"] = ""
            context["p3_text"] = ""

        events = BiographyEvent.objects.all()
        context["events"] = events
        return context


class Section3View1(TemplateView):
    template_name = "html/section3__DOB/sek3__1.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем данные в контекст, если это необходимо
        gallery = Gallery1.objects.first()
        context["gallery"] = gallery
        return context


class Section3View2(TemplateView):
    template_name = "html/section3__DOB/sek3__2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем данные в контекст, если это необходимо
        gallery = Gallery2.objects.first()
        context["gallery"] = gallery
        return context


class Section3View3(TemplateView):
    template_name = "html/section3__DOB/sek3__3.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем данные в контекст, если это необходимо
        gallery = Gallery3.objects.first()
        context["gallery"] = gallery
        return context


class Section3View4(TemplateView):
    template_name = "html/section3__DOB/sek3__4.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем данные в контекст, если это необходимо
        gallery = Gallery4.objects.first()
        context["gallery"] = gallery
        return context


class Section3View5(TemplateView):
    template_name = "html/section3__DOB/sek3__5.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем данные в контекст, если это необходимо
        gallery = Gallery5.objects.first()
        context["gallery"] = gallery
        return context


class ContactCreateView(CreateView):
    model = Contact
    fields = ["name", "number", "comment"]
    template_name = "form_template.html"  # Шаблон для отображения формы
    success_url = reverse_lazy("success")
