from rest_framework import viewsets
from polls.models import Poll, Question, UserAnswer
from polls.serializers import PollSerializer, QuestionSerializer
from rest_framework import permissions


# Create your views here.


class PollView(viewsets.ModelViewSet):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()

    permission_classes_by_action = {
        'create': [permissions.IsAdminUser],
        'list': [permissions.IsAuthenticatedOrReadOnly]
    }

    def create(self, request, *args, **kwargs):
        return super(PollView, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(PollView, self).list(request, *args, **kwargs)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class QuestionView(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
