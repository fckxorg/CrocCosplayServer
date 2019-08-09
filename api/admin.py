from django.contrib import admin
from .models import Event, Character, SubEvent, Fight, Ability, CosplayElement, AttendedCharacter

admin.site.register(Event)
admin.site.register(Character)
admin.site.register(SubEvent)
admin.site.register(Fight)
admin.site.register(Ability)
admin.site.register(CosplayElement)
admin.site.register(AttendedCharacter)
# Register your models here.
