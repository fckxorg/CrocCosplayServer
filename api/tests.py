from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Event, SubEvent, Fight, Character
from .views import get_events, get_event, get_character, select_character, select_fight
# Create your tests here.


class Event(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", email="test@test.com", password="/dev/null")
        for i in range(2):
            curr = SubEvent(name="test_subevent_"+str(i), description="test_subevent_description", date="2019-08-09 13:45:32")
            curr.save()
        for i in range(2):
            curr = Fight(name="test_fight_"+str(i), date="2019-08-09 13:45:32", picture=SimpleUploadedFile("fight_picture_"+str(i)+".png", bytes(str(i)*5, encoding='utf-8')))
            curr.save()
        for i in range(2):
            curr = Character(name="test_character_"+str(i), picture=SimpleUploadedFile("character_picture_"+str(i)+".png", bytes(str(i)*5, encoding='utf-8')))
            curr.save()
        event = Event(name="test_event", date="2019-08-09 13:45:32")
        event.save()
        event.sub_events.set(SubEvent.objects.all())
        event.fights.set(Fight.objects.all())
        event.characters.set(Character.objects.all())
        event.save()

    def test_getting_events(self):
        factory = RequestFactory()
        request = factory.get("api/events/")
        request.user = self.user
        response = get_events(request)
        self.assertEqual(response.status_code, 200)