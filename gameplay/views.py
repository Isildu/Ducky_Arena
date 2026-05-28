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
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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


@api_view(['POST'])
def resolve_answer(request):
    question_id = request.data.get('question_id')
    selected_answer_id = request.data.get('selected_answer_id')
    attacker_character_id = request.data.get('attacker_character_id')

    if not question_id or not selected_answer_id or not attacker_character_id:
        return Response(
            {'detail': 'question_id, selected_answer_id and attacker_character_id are required.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        question = Question.objects.get(id=question_id)
        selected_answer = AnswerOption.objects.get(id=selected_answer_id, question=question)
        attacker = Character.objects.get(id=attacker_character_id)
    except Question.DoesNotExist:
        return Response({'detail': 'Question not found.'}, status=status.HTTP_404_NOT_FOUND)
    except AnswerOption.DoesNotExist:
        return Response({'detail': 'Answer option not found for this question.'}, status=status.HTTP_404_NOT_FOUND)
    except Character.DoesNotExist:
        return Response({'detail': 'Attacker character not found.'}, status=status.HTTP_404_NOT_FOUND)

    is_correct = selected_answer.is_correct

    if is_correct:
        damage = attacker.base_damage
        message = f'Respuesta correcta. {attacker.name} inflige {damage} de daño.'
    else:
        damage = 0
        message = f'Respuesta incorrecta. {attacker.name} no inflige daño.'

    return Response({
        'correct': is_correct,
        'damage': damage,
        'attacker': attacker.name,
        'question': question.text,
        'selected_answer': selected_answer.text,
        'message': message
    })