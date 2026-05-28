from django.db import models
from django.contrib.auth.models import User # Importación limpia arriba del todo

# ==========================================
# 1. TABLAS BASE DE GAMEPLAY (Tus primeras 3 tablas)
# ==========================================

class GameMap(models.Model):
    name = models.CharField(max_length=50)
    max_players = models.IntegerField(default=8)
    theme = models.CharField(max_length=30)

    class Meta:
        db_table = 'game_maps'

class Character(models.Model):
    name = models.CharField(max_length=30)
    base_health = models.IntegerField(default=100)
    base_speed = models.IntegerField(default=10)

    class Meta:
        db_table = 'characters'

class Ability(models.Model):
    name = models.CharField(max_length=30)
    damage = models.IntegerField(default=0)
    cooldown = models.FloatField(default=0.0)

    class Meta:
        db_table = 'abilities'


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
    map = models.ForeignKey(GameMap, on_delete=models.CASCADE)
    duration_seconds = models.IntegerField()
    played_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'matches'

class MatchPlayer(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    profile = models.ForeignKey('PlayerProfile', on_delete=models.CASCADE, related_name='match_performances')
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    class Meta:
        db_table = 'match_players'

class PlayerFriend(models.Model):
    profile = models.ForeignKey('PlayerProfile', on_delete=models.CASCADE, related_name='friendships')
    friend = models.ForeignKey('PlayerProfile', on_delete=models.CASCADE, related_name='friended_by')
    became_friends_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'player_friends'