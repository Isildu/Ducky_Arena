from django.db import models
from django.contrib.auth.models import User # Importación limpia arriba del todo

# ==========================================
# 1. TABLAS BASE DE GAMEPLAY (Tus primeras 3 tablas)
# ==========================================

class GameMap(models.Model):
    name = models.CharField(max_length=50)
    max_players = models.IntegerField(default=6)
    theme = models.CharField(max_length=30)
    lanes = models.IntegerField(default=3)

    class Meta:
        db_table = 'game_maps'

    def __str__(self):
        return self.name

class Character(models.Model):
    ROLE_CHOICES = [
        ('hacker', 'Hacker/Debuffer'),
        ('tank', 'Tank/Control'),
        ('mage', 'Mage/Burst'),
        ('healer', 'Healer/DPS'),
        ('support', 'Support/Buffer'),
    ]

    name = models.CharField(max_length=30)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='hacker'
    )
    base_health = models.IntegerField(default=100)
    base_damage = models.IntegerField(default=10)
    base_stamina = models.IntegerField(default=10)
    base_defense = models.IntegerField(default=5)
    base_support = models.IntegerField(default=0)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'characters'

    def __str__(self):
        return self.name

class Ability(models.Model):
    ABILITY_TYPE_CHOICES = [
        ('attack', 'Attack'),
        ('defense', 'Defense'),
        ('buff', 'Buff'),
        ('debuff', 'Debuff'),
        ('heal', 'Heal'),
    ]

    character = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        related_name='abilities',
        null=True,
        blank=True
    )    
    name = models.CharField(max_length=50)
    ability_type = models.CharField(
        max_length=20,
        choices=ABILITY_TYPE_CHOICES,
        default='attack'
    )
    power = models.IntegerField(default=0)
    cooldown = models.IntegerField(default=0)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'abilities'

    def __str__(self):
        return self.name


# ==========================================
# 2. TABLAS DE JUGADOR Y PROGRESO (Las tablas de Oriol)
# ==========================================

class PlayerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField(max_length=20, null=True, blank=True)
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    bread_coins = models.IntegerField(default=0)

    class Meta:
        db_table = 'player_profile'

class Cosmetic(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    price = models.IntegerField()

    class Meta:
        db_table = 'cosmetics'

class PlayerCosmetic(models.Model):
    profile = models.ForeignKey('PlayerProfile', on_delete=models.CASCADE, related_name='cosmetics')
    cosmetic = models.ForeignKey(Cosmetic, on_delete=models.CASCADE)
    unlocked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'player_cosmetics'
        unique_together = ('profile', 'cosmetic')

class DailyQuest(models.Model):
    description = models.CharField(max_length=140)
    reward_coins = models.IntegerField()

    class Meta:
        db_table = 'daily_quest'

class PlayerQuest(models.Model):
    profile = models.ForeignKey('PlayerProfile', on_delete=models.CASCADE, related_name='quests')
    quest = models.ForeignKey(DailyQuest, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'player_quests'


# ==========================================
# 3. TABLAS DE HISTORIAL Y RELACIONES (Tus últimas 3 tablas enlazadas)
# ==========================================

class Match(models.Model):
    STATUS_CHOICES = [
        ('waiting', 'Waiting'),
        ('lane_selection', 'Lane Selection'),
        ('in_progress', 'In Progress'),
        ('finished', 'Finished'),
    ]

    WINNER_CHOICES = [
        ('blue', 'Blue Team'),
        ('red', 'Red Team'),
        ('draw', 'Draw'),
    ]

    map = models.ForeignKey(GameMap, on_delete=models.CASCADE)
    mode = models.CharField(max_length=30, default='Survival')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='waiting')
    winner_team = models.CharField(max_length=10, choices=WINNER_CHOICES, null=True, blank=True)
    duration_seconds = models.IntegerField(default=0)
    played_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'matches'

class MatchPlayer(models.Model):
    TEAM_CHOICES = [
        ('blue', 'Blue Team'),
        ('red', 'Red Team'),
    ]

    LANE_CHOICES = [
        ('top', 'Top Lane'),
        ('mid', 'Mid Lane'),
        ('bot', 'Bot Lane'),
    ]

    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='players')
    profile = models.ForeignKey(PlayerProfile, on_delete=models.CASCADE, related_name='match_performances')
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    team = models.CharField(max_length=10, choices=TEAM_CHOICES)
    selected_lane = models.CharField(max_length=10, choices=LANE_CHOICES)
    remaining_health = models.IntegerField(default=100)
    score = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    wrong_answers = models.IntegerField(default=0)

    class Meta:
        db_table = 'match_players'
        unique_together = ('match', 'profile')

class PlayerFriend(models.Model):
    profile = models.ForeignKey('PlayerProfile', on_delete=models.CASCADE, related_name='friendships')
    friend = models.ForeignKey('PlayerProfile', on_delete=models.CASCADE, related_name='friended_by')
    became_friends_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'player_friends'



class QuestionCategory(models.Model):
    name = models.CharField(max_length=50)
    required_level = models.IntegerField(default=1)

    class Meta:
        db_table = 'question_categories'

    def __str__(self):
        return self.name


class Question(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    category = models.ForeignKey(QuestionCategory, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    correct_answer = models.CharField(max_length=255)

    class Meta:
        db_table = 'questions'

    def __str__(self):
        return self.text[:50]


class AnswerOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    class Meta:
        db_table = 'answer_options'

    def __str__(self):
        return self.text