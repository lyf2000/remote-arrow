from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView

from remote_arrows.service import ArrowControlAdapter

# Create your views here.


class ControlPageView(TemplateView):
    ACTIONS_ENABLED = ["up", "down", "left", "right"]
    template_name = "core/control_page.html"

    def get(self, request, slug=None, *args, **kwargs):
        if slug is None:
            return super().get(request, *args, **kwargs)

        if slug not in self.ACTIONS_ENABLED:
            return HttpResponseBadRequest(f"Action {slug} not found!")
        self.get_action(slug)
        return JsonResponse({})

    def get_action(self, action: str):
        ArrowControlAdapter.click_keyb(action)
