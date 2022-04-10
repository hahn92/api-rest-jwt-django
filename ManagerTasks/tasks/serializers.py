from rest_framework import serializers

# models
from .models import Tasks

class TasksSerializer(serializers.ModelSerializer):
    tasks_author = serializers.ReadOnlyField(source='tasks_author.username')
    
    class Meta:
        model = Tasks
        fields = ('id', 'title', "description", "tasks_state", "tasks_author", "created", "modified")
        extra_kwargs = {
            "title": {"required": True, "allow_blank": False}, 
            "description": {"required": True, "allow_blank": False},
            "tasks_state": {"required": True, "allow_blank": False},
        }

