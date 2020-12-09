from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
import datetime


# default values
DEFAULT_COUNTRY_ID = 1
DEFAULT_WAVE = 1
DEFAULT_POINT = Point(0, 0, srid=4326)
DEFAULT_PAGE_DISPLAY_NAME = 'UNKNOWN MISSILE'
DEFAULT_WEAPON_TYPE = 'ICBM'
DEFAULT_MESSAGE_COUNTRY_CODE = 'XXX'


class Scenario(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    exercise_start = models.DateTimeField(default=datetime.datetime.now)
    scenario_start = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.name


class Weapon(models.Model):
    country = models.ForeignKey('world.WorldBorder', on_delete=models.CASCADE, default=DEFAULT_COUNTRY_ID)
    wave = models.CharField(max_length=2, default=DEFAULT_WAVE)
    launch_location = models.PointField(default=DEFAULT_POINT)
    launch_datetime = models.DateTimeField(default=datetime.datetime.now)
    page_display_name = models.CharField(max_length=200, default=DEFAULT_PAGE_DISPLAY_NAME)
    message_weapon_type = models.CharField(max_length=200, default=DEFAULT_WEAPON_TYPE)
    message_country_code = models.CharField(max_length=10, default=DEFAULT_MESSAGE_COUNTRY_CODE)


class Warhead(models.Model):
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, related_name='warheads')
    warhead_yield = models.FloatField(default=0)
    impact_location = models.PointField(default=DEFAULT_POINT)
    impact_datetime = models.DateTimeField(default=datetime.datetime.now)
    message_country_code = models.CharField(max_length=10, default=DEFAULT_MESSAGE_COUNTRY_CODE)

