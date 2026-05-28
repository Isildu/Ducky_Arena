from rest_framework import viewsets
from .models import GameMap, Character, Ability, Match, MatchPlayer, PlayerFriend, Question, QuestionCategory, AnswerOption
from .serializers import (
    GameMapSerializer, CharacterSerializer, AbilitySerializer,
    MatchSerializer, MatchPlayerSerializer, PlayerFriendSerializer,
    QuestionSerializer, QuestionCategorySerializer, AnswerOptionSerializer
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
import random

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

class QuestionCategoryViewSet(viewsets.ModelViewSet):
    queryset = QuestionCategory.objects.all()
    serializer_class = QuestionCategorySerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @action(detail=False, methods=['get'])
    def random(self, request):
        category = request.query_params.get('category')
        difficulty = request.query_params.get('difficulty')

        questions = Question.objects.all()

        if category:
            questions = questions.filter(category__name__iexact=category)

        if difficulty:
            questions = questions.filter(difficulty__iexact=difficulty)

        question = questions.order_by('?').first()

        if not question:
            return Response(
                {'detail': 'No questions found for the selected filters.'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(question)
        return Response(serializer.data)


class AnswerOptionViewSet(viewsets.ModelViewSet):
    queryset = AnswerOption.objects.all()
    serializer_class = AnswerOptionSerializer