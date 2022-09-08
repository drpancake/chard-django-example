from django.views import View
from django.shortcuts import render

from .tasks import get_itunes_charts
from .models import ChartRank


class ChartsView(View):
    def _render(self, request):
        context = dict(chart_ranks=ChartRank.objects.all().order_by("-pk"))
        return render(request, "charts.html", context=context)

    def get(self, request):
        return self._render(request)

    def post(self, request):
        get_itunes_charts.send("gb")
        get_itunes_charts.send("us")
        get_itunes_charts.send("de")
        get_itunes_charts.send("it")
        get_itunes_charts.send("fr")
        get_itunes_charts.send("jp")
        get_itunes_charts.send("ca")
        get_itunes_charts.send("au")
        return self._render(request)
