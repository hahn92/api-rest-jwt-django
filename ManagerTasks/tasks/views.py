from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .serializers import TasksSerializer
from .pagination import CustomPagination
from .permission import IsOwnerOrReadOnly
from .models import Tasks


class ListCreateTasksAPIView(ListCreateAPIView):
    """
    - Consulta tareas (search: espesifica el texto a buscar dentro de la descripcion)
    - Crea una nueva tarea
    """
    serializer_class = TasksSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    
    def get_queryset(self):
        queryset = Tasks.objects.filter(tasks_author=self.request.user, is_active=True)
        keywords = self.request.query_params.get('search')
        if keywords:
            queryset = Tasks.objects.filter(description__contains=keywords)
        return queryset
        
    def perform_create(self, serializer):
        serializer.save(tasks_author=self.request.user)


class RetrieveUpdateDestroyTasksAPIView(RetrieveUpdateDestroyAPIView):
    """
    - Actualiza una tarea
    - Elimina una tarea
    """
    serializer_class = TasksSerializer
    queryset = Tasks.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]