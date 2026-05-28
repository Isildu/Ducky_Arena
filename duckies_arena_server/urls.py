from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from gameplay.views import (
    GameMapViewSet, CharacterViewSet, AbilityViewSet,
    MatchViewSet, MatchPlayerViewSet, PlayerFriendViewSet,
    resolve_answer
)

# El router de Django REST Framework genera las URLs automáticamente
router = DefaultRouter()
router.register(r'maps', GameMapViewSet)
router.register(r'characters', CharacterViewSet)
router.register(r'abilities', AbilityViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'match-players', MatchPlayerViewSet)
router.register(r'friends', PlayerFriendViewSet)

from gameplay.views import (
    PlayerProfileViewSet, CosmeticViewSet, PlayerCosmeticViewSet,
    DailyQuestViewSet, PlayerQuestViewSet, QuestionCategoryViewSet, 
    QuestionViewSet, AnswerOptionViewSet
)

# ... (donde tienes tus otros router.register, añade estos 5 abajo) ...
router.register(r'profiles', PlayerProfileViewSet)
router.register(r'cosmetics', CosmeticViewSet)
router.register(r'player-cosmetics', PlayerCosmeticViewSet)
router.register(r'quests', DailyQuestViewSet)
router.register(r'player-quests', PlayerQuestViewSet)
router.register(r'question-categories', QuestionCategoryViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answer-options', AnswerOptionViewSet)

# Todas tus rutas colgarán de /api/
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/combat/resolve-answer/', resolve_answer),
]