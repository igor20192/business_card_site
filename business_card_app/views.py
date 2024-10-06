import logging
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .models import (
    Contact,
    EventBlock,
    Footer,
    Gallery1,
    Gallery2,
    Gallery3,
    Gallery4,
    Gallery5,
    BiographyEvent,
    Video,
)

# Настройка логирования
logger = logging.getLogger(__name__)


class MainView(TemplateView):
    """
    Displays the main page of the website with data from the Footer model and events from the BiographyEvent model.

    Attributes:
        template_name (str): Path to the template for rendering.

    Methods:
        get_context_data(self, **kwargs): Adds Footer and BiographyEvent data to the context.
    """

    template_name = "html/main.html"

    def get_context_data(self, **kwargs):
        """
        Retrieves data for the page context, including footer text and biography events.

        Returns:
            dict: Context containing footer text and a list of biography events.
        """
        context = super().get_context_data(**kwargs)
        try:
            footer = Footer.objects.first()  # Retrieve the first footer entry
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
            context["eventblock"] = EventBlock.objects.first()
            context["videos"] = Video.objects.all()

        except Footer.DoesNotExist as e:
            logger.error(f"Footer data not found: {e}")
            context["div_text"] = context["p1_text"] = context["p2_text"] = context[
                "p3_text"
            ] = ""
        except BiographyEvent.DoesNotExist as e:
            logger.error(f"BiographyEvent data not found: {e}")
            context["events"] = []
        except Exception as e:
            logger.exception(f"An unexpected error occurred in MainView: {e}")
            context["div_text"] = context["p1_text"] = context["p2_text"] = context[
                "p3_text"
            ] = ""
            context["events"] = []
        return context


class Section3View1(TemplateView):
    """
    Displays the Section 3 page with the first gallery (Gallery1).

    Attributes:
        template_name (str): Path to the template for rendering.

    Methods:
        get_context_data(self, **kwargs): Adds the first gallery (Gallery1) data to the context.
    """

    template_name = "html/section3__DOB/sek3__1.html"

    def get_context_data(self, **kwargs):
        """
        Retrieves data for the page context, including the first gallery.

        Returns:
            dict: Context containing the first gallery object.
        """
        context = super().get_context_data(**kwargs)
        try:
            gallery = Gallery1.objects.prefetch_related("images").first()
            context["gallery"] = gallery
        except Gallery1.DoesNotExist as e:
            logger.error(f"Gallery1 data not found: {e}")
            context["gallery"] = None
        except Exception as e:
            logger.exception(f"An unexpected error occurred in Section3View1: {e}")
            context["gallery"] = None
        return context


class Section3View2(TemplateView):
    """
    Displays the Section 3 page with the second gallery (Gallery2).

    Attributes:
        template_name (str): Path to the template for rendering.

    Methods:
        get_context_data(self, **kwargs): Adds the second gallery (Gallery2) data to the context.
    """

    template_name = "html/section3__DOB/sek3__2.html"

    def get_context_data(self, **kwargs):
        """
        Retrieves data for the page context, including the second gallery.

        Returns:
            dict: Context containing the second gallery object.
        """
        context = super().get_context_data(**kwargs)
        try:
            gallery = Gallery2.objects.prefetch_related("images").first()
            context["gallery"] = gallery
        except Gallery2.DoesNotExist as e:
            logger.error(f"Gallery2 data not found: {e}")
            context["gallery"] = None
        except Exception as e:
            logger.exception(f"An unexpected error occurred in Section3View2: {e}")
            context["gallery"] = None
        return context


class Section3View3(TemplateView):
    """
    Displays the Section 3 page with the third gallery (Gallery3).

    Attributes:
        template_name (str): Path to the template for rendering.

    Methods:
        get_context_data(self, **kwargs): Adds the third gallery (Gallery3) data to the context.
    """

    template_name = "html/section3__DOB/sek3__3.html"

    def get_context_data(self, **kwargs):
        """
        Retrieves data for the page context, including the third gallery.

        Returns:
            dict: Context containing the third gallery object.
        """
        context = super().get_context_data(**kwargs)
        try:
            gallery = Gallery3.objects.prefetch_related("images").first()
            context["gallery"] = gallery
        except Gallery3.DoesNotExist as e:
            logger.error(f"Gallery3 data not found: {e}")
            context["gallery"] = None
        except Exception as e:
            logger.exception(f"An unexpected error occurred in Section3View3: {e}")
            context["gallery"] = None
        return context


class Section3View4(TemplateView):
    """
    Displays the Section 3 page with the fourth gallery (Gallery4).

    Attributes:
        template_name (str): Path to the template for rendering.

    Methods:
        get_context_data(self, **kwargs): Adds the fourth gallery (Gallery4) data to the context.
    """

    template_name = "html/section3__DOB/sek3__4.html"

    def get_context_data(self, **kwargs):
        """
        Retrieves data for the page context, including the fourth gallery.

        Returns:
            dict: Context containing the fourth gallery object.
        """
        context = super().get_context_data(**kwargs)
        try:
            gallery = Gallery4.objects.prefetch_related("images").first()
            context["gallery"] = gallery
        except Gallery4.DoesNotExist as e:
            logger.error(f"Gallery4 data not found: {e}")
            context["gallery"] = None
        except Exception as e:
            logger.exception(f"An unexpected error occurred in Section3View4: {e}")
            context["gallery"] = None
        return context


class Section3View5(TemplateView):
    """
    Displays the Section 3 page with the fifth gallery (Gallery5).

    Attributes:
        template_name (str): Path to the template for rendering.

    Methods:
        get_context_data(self, **kwargs): Adds the fifth gallery (Gallery5) data to the context.
    """

    template_name = "html/section3__DOB/sek3__5.html"

    def get_context_data(self, **kwargs):
        """
        Retrieves data for the page context, including the fifth gallery.

        Returns:
            dict: Context containing the fifth gallery object.
        """
        context = super().get_context_data(**kwargs)
        try:
            gallery = Gallery5.objects.prefetch_related("images").first()
            context["gallery"] = gallery
        except Gallery5.DoesNotExist as e:
            logger.error(f"Gallery5 data not found: {e}")
            context["gallery"] = None
        except Exception as e:
            logger.exception(f"An unexpected error occurred in Section3View5: {e}")
            context["gallery"] = None
        return context


class ContactCreateView(CreateView):
    """
    View for creating a record in the Contact model.

    Attributes:
        model (Model): The model used to create the object.
        fields (list): The model fields that will be displayed in the form.
        template_name (str): Template used to display the form.
        success_url (str): URL to redirect to upon successful creation.
    """

    model = Contact
    fields = ["name", "number", "comment"]
    template_name = "form_template.html"  # Template for rendering the form
    success_url = reverse_lazy(
        "success"
    )  # Redirect to success page after form submission

    def form_valid(self, form):
        """
        Logs the success of form validation and handles any exceptions during the save process.

        Returns:
            HttpResponse: Redirect to the success page on successful form submission.
        """
        try:
            response = super().form_valid(form)
            logger.info(f"Contact form submitted successfully for {form.instance.name}")
            return response
        except Exception as e:
            logger.exception(f"Error occurred while saving contact form: {e}")
            form.add_error(None, "An unexpected error occurred. Please try again.")
            return self.form_invalid(form)
