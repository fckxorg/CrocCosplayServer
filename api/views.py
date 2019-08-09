from django.shortcuts import render
from .models import Character, Event, SubEvent, CosplayElement, Fight, AttendedCharacter
import base64
from django.http.response import JsonResponse


# Create your views here.

def get_events(request):
    events = Event.objects.all()
    data = {"events": []}
    for event in events:
        data["events"].append({"name": event.name,
                               "uuid": event.uuid,
                               "date": str(event.date),
                               "members_count": event.members.all().count(),
                               "picture": str(base64.b64encode(event.picture.read()))[2:-1]})
    return JsonResponse(data)


def get_event(request, event_id):
    event = Event.objects.get(uuid=event_id)
    data = {
        "uuid": event_id,
        "name": event.name,
        "description": event.description,
        "date": str(event.date),
        "picture": str(base64.b64encode(event.picture.read()))[2:-1],
        "subevents": [],
        "fights": [],
        "characters": []
    }

    for subevent in event.sub_events.all():
        data["subevents"].append({
            "uuid": subevent.uuid,
            "name": subevent.name,
            "description": subevent.description,
            "date": str(subevent.date)
        })

    for fight in event.fights.all():
        data["fights"].append({
            "uuid": fight.uuid,
            "name": event.name,
            "date": fight.date,
            "picture": str(base64.b64encode(fight.picture.read()))[2:-1]
        })

    for character in event.characters.all():
        data["characters"].append({
            "uuid": character.uuid,
            "name": character.name,
            "picture": str(base64.b64encode(fight.picture.read()))[2:-1]
        })
    return JsonResponse(data)


def get_character(request, uuid):
    character = Character.objects.get(uuid=uuid)
    data = {
        "uuid": character.uuid,
        "name": character.name,
        "picture": str(base64.b64encode(character.picture.read()))[2:-1],
        "description": character.description,
        "abilities": [],
        "cosplayelements": []
    }
    for ability in character.abilities.all():
        data["abilities"].append({
            "uuid": ability.uuid,
            "name": ability.name,
            "description": ability.description,
            "damage": ability.damage,
            "picture": str(base64.b64encode(ability.picture.read()))[2:-1]
        })

    for cosplay_element in character.cosplay_elements.all():
        data["cosplayelements"].append({
            "uuid": cosplay_element.uuid,
            "name": cosplay_element.name,
            "cost": cosplay_element.cost,
            "url": cosplay_element.url
        })
    return JsonResponse(data)


def select_character(request, event_uuid, character_uuid):
    character = Character.objects.get(uuid=character_uuid)
    event = Event.objects.get(uuid=event_uuid)
    event.members.add(request.user)
    entry = AttendedCharacter(character=character, user=request.user, event=Event.objects.get(uuid=event_uuid))
    entry.save()
    return JsonResponse({"status": "Ok"})


def select_fight(request, fight_uuid, flag):
    fight = Fight.objects.get(uuid=fight_uuid)
    if flag == 1:
        fight.team_good.add(request.user)
    else:
        fight.team_evil.add(request.user)
    return JsonResponse({"status": "Ok"})
