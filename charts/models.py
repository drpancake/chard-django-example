from django.db import models


class ChartRank(models.Model):
    itunes_id = models.BigIntegerField()
    position = models.PositiveSmallIntegerField()
    country_code = models.CharField(max_length=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.itunes_id)
