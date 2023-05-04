from django.http import Http404, HttpResponseRedirect
from django.db import transaction
from django.views.generic import CreateView
from django.urls import reverse
from django.shortcuts import redirect

from .models import RedirectModel

# Create your views here.


def redirec_url_from_shortened_link_view(request, short_code):
    """
    redirect from shortened link to long URL and increase visit counter
    """
    try:
        with transaction.atomic():
            model_instance = RedirectModel.objects.get(short_code=short_code)
            model_instance.visit_counter += 1
            model_instance.save()

            return HttpResponseRedirect(model_instance.url)
    except RedirectModel.DoesNotExist:
        raise Http404("لینک خراب است")


class CreateShortenedLinkCreateView(CreateView):
    """
    Create a shortened link from a long URL
    """

    model = RedirectModel
    template_name = "create_shortened_link.html"
    fields = ["url"]
    success_url = "have-shortened-link"

    def get(self, request, *args, **kwargs):
        """
        change short_code query string if have not instance of RedirectModel
        """
        if kwargs:
            try:
                short_code = self.kwargs.get("short_code")
                RedirectModel.objects.get(short_code=short_code)
            except RedirectModel.DoesNotExist:
                return redirect(reverse("create-shortened-link"))
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        """
        return to current page with short_code in query string
        """
        return reverse(
            self.success_url, kwargs={"short_code": self.object.short_code}
        )

    def get_context_data(self, **kwargs):
        """
        pass query string and base_url to template
        """
        context = super().get_context_data(**kwargs)
        try:
            context["short_code"] = self.kwargs.get("short_code")
            context["base_url"] = self.request.build_absolute_uri("/")
        except:
            pass
        return context
