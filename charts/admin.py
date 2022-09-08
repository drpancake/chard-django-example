from django.contrib import admin

from .models import ChartRank


class ChartRankAdmin(admin.ModelAdmin):
    list_display = ("itunes_id", "position", "country_code", "created")


admin.site.register(ChartRank, ChartRankAdmin)
