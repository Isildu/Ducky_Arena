from rest_framework import viewsets
from .models import GameMap, Character, Ability, Match, MatchPlayer, PlayerFriend
from .serializers import (
    GameMapSerializer, CharacterSerializer, AbilitySerializer,
    MatchSerializer, MatchPlayerSerializer, PlayerFriendSerializer
)

class GameMapViewSet(viewsets.ModelViewSet):
    queryset = GameMap.objects.all()
    serializer_class = GameMapSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class AbilityViewSet(viewsets.ModelViewSet):
    queryset = Ability.objects.all()
    serializer_class = AbilitySerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class MatchPlayerViewSet(viewsets.ModelViewSet):
    queryset = MatchPlayer.objects.all()
    serializer_class = MatchPlayerSerializer

class PlayerFriendViewSet(viewsets.ModelViewSet):
    queryset = PlayerFriend.objects.all()
    serializer_class = PlayerFriendSerializer

from .models import PlayerProfile, Cosmetic, PlayerCosmetic, DailyQuest, PlayerQuest
from .serializers import (
    PlayerProfileSerializer, CosmeticSerializer, PlayerCosmeticSerializer,
    DailyQuestSerializer, PlayerQuestSerializer
)

class PlayerProfileViewSet(viewsets.ModelViewSet):
    queryset = PlayerProfile.objects.all()
    serializer_class = PlayerProfileSerializer

class CosmeticViewSet(viewsets.ModelViewSet):
    queryset = Cosmetic.objects.all()
    serializer_class = CosmeticSerializer

class PlayerCosmeticViewSet(viewsets.ModelViewSet):
    queryset = PlayerCosmetic.objects.all()
    serializer_class = PlayerCosmeticSerializer

class DailyQuestViewSet(viewsets.ModelViewSet):
    queryset = DailyQuest.objects.all()
    serializer_class = DailyQuestSerializer

class PlayerQuestViewSet(viewsets.ModelViewSet):
    queryset = PlayerQuest.objects.all()
    serializer_class = PlayerQuestSerializer