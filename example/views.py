from django.contrib import admin

from edc_base.views.edc_base_view_mixin import EdcBaseViewMixin
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class HomeView(EdcBaseViewMixin, TemplateView):
    template_name = 'example/home.html'
    app_config_name = 'example'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            site_header=admin.site.site_header,
        )
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)
