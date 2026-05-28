from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from gameplay.views import (
    GameMapViewSet, CharacterViewSet, AbilityViewSet,
    MatchViewSet, MatchPlayerViewSet, PlayerFriendViewSet
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
    DailyQuestViewSet, PlayerQuestViewSet
)

# ... (donde tienes tus otros router.register, añade estos 5 abajo) ...
router.register(r'profiles', PlayerProfileViewSet)
router.register(r'cosmetics', CosmeticViewSet)
router.register(r'player-cosmetics', PlayerCosmeticViewSet)
router.register(r'quests', DailyQuestViewSet)
router.register(r'player-quests', PlayerQuestViewSet)

urlpatterns = [
    path('admin/', admin.site.viewsets if hasattr(admin, 'viewsets') else admin.site.urls),
    path('api/', include(router.urls)), # Todas tus rutas colgarán de /api/
]