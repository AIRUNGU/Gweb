from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from Gapp import models as G_models
# Register your models here.

@admin.register(G_models.Articles)
class ArticleAdmin(LeafletGeoAdmin):
	pass
@admin.register(G_models.Event)
class EventAdmin(LeafletGeoAdmin):
	pass
admin.site.register(G_models.Category)
admin.site.register(G_models.Announcements)
# admin.site.register(G_models.Event)