from django.contrib import admin
from .models import *

admin.site.register(Character)
admin.site.register(Ability)
admin.site.register(GameMap)
admin.site.register(Match)
admin.site.register(MatchPlayer)
admin.site.register(PlayerProfile)
admin.site.register(PlayerFriend)
admin.site.register(Cosmetic)
admin.site.register(PlayerCosmetic)
admin.site.register(DailyQuest)
admin.site.register(PlayerQuest)
admin.site.register(QuestionCategory)
admin.site.register(Question)
admin.site.register(AnswerOption)