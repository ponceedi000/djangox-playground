from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import PlayGround


class PlayGroundListView(ListView):
    template_name = "play_ground/play_ground-list.html"
    model = PlayGround


class PlayGroundDetailView(DetailView):
    template_name = "play_ground/play_ground-detail.html"
    model = PlayGround


class PlayGroundCreateView(CreateView):
    template_name = "play_ground/play_ground-create.html"
    model = PlayGround
    fields = ['name', 'description', 'author']


class PlayGroundUpdateView(UpdateView):
    template_name = "play_ground/play_ground-update.html"
    model = PlayGround
    fields = ['name', 'description', 'author']


class PlayGroundDeleteView(DeleteView):
    template_name = "play_ground/play_ground-delete.html"
    model = PlayGround
    success_url = reverse_lazy("_list")
