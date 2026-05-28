from rest_framework import serializers
from .models import GameMap, Character, Ability, Match, MatchPlayer, PlayerFriend, Question, QuestionCategory, AnswerOption

class GameMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameMap
        fields = '__all__'

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'

class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class MatchPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchPlayer
        fields = '__all__'

class PlayerFriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerFriend
        fields = '__all__'
from .models import PlayerProfile, Cosmetic, PlayerCosmetic, DailyQuest, PlayerQuest

class PlayerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerProfile
        fields = '__all__'

class CosmeticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cosmetic
        fields = '__all__'

class PlayerCosmeticSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerCosmetic
        fields = '__all__'

class DailyQuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyQuest
        fields = '__all__'

class PlayerQuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerQuest
        fields = '__all__'

class QuestionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionCategory
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerOption
        fields = '__all__'