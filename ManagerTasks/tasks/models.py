# Django
from django.db import models

# Custom User
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class TemplateTasks(models.Model):

    is_active = models.BooleanField(
        default=True,
        verbose_name='Activo',
    )
    # Logs
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Creado'
    )
    modified = models.DateTimeField(
        auto_now=True,
        verbose_name='Modificado'
    )

    class Meta:
        abstract = True


class Tasks(TemplateTasks):

    title = models.CharField(
        max_length=50,
        default="",
        blank=False,
        null=False,
        verbose_name='Titulo',
    )

    tasks_author = models.ForeignKey(
        User,
        related_name="tasks_author",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        verbose_name='Autor',
        default=""
    )

    description = models.TextField(
        max_length=500,
        default="",
        blank=True,
        null=True,
        verbose_name='Descripción',
    )

    states = (
        ('', ''),
        ('Completa', 'Completa'),
        ('Incompleta', 'Incompleta'),
    )

    tasks_state = models.CharField(
        max_length=20,
        choices=states,
        default="",
        blank=True,
        null=True,
        verbose_name='Estado tarea'
    )

    def __str__(self):
        return "{} - {} - {}".format(self.id, self.title, self.tasks_author)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        permissions = (
            ("view_all_tasks", "Can view all tasks"),
        )

