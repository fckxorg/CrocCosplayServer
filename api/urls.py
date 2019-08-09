from django.urls import path

from . import views

urlpatterns = [
    path('events/', views.get_events, name='get_events'),
    path('events/<int:event_id>/', views.get_event, name="get_event"),
    path('character/<int:uuid>/', views.get_character, name="get_character"),
    path('character/attend/<int:event_uuid>/<int:character_uuid>/', views.select_character, name="select_character"),
    path('fight/join/<int:fight:uuid>/', views.select_fight, name="select_fight")
]