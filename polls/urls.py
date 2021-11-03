from rest_framework import routers
from polls.views import PollView

router = routers.DefaultRouter()
router.register('polls', viewset=PollView)

urlpatterns = router.urls
