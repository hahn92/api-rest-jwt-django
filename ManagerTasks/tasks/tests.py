# Django
from django.test import TestCase

# Python
import json

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status


# Custom User
from django.contrib.auth import get_user_model
User = get_user_model()    


# Models
from .models import Tasks

class TaskTestCase(TestCase):

    def setUp(self):
        """
        Setup para las pruebas
        """
        user = User(
            username='admin'
        )
        user.set_password('admin123')
        user.save()

        client = APIClient()
        response = client.post(
                '/api/token/', {
                'username': 'admin',
                'password': 'admin123',
            },
            format='json'
        )

        result = json.loads(response.content)
        self.user = user
        self.access = result['access']
        self.refresh = result['refresh']
    

    def test_create_task(self):
        """
        Crear una tarea
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access)

        test_task = {
            "title": "Titulo 0",
            "description": "Descripcion 0",
            "tasks_state": ""
        }

        response = client.post(
            '/api/v1/tasks/', 
            test_task,
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(result['title'], test_task['title'])


    def test_update_task(self):
        """
        Test actualizacion tareas
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access)

        tasks = Tasks.objects.create(
            title='Titulo 1',
            description='Descripcion 1',
            tasks_state='',
            tasks_author=self.user
        )

        test_tasks_update = {
            'title': 'Titulo 2',
            'description': 'Descripcion 2',
            'tasks_state': 'Completa',
        }

        response = client.put(
            f'/api/v1/tasks/{tasks.pk}', 
            test_tasks_update,
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        if 'pk' in result:
            del result['pk']

        self.assertEqual(result['title'], test_tasks_update['title'])

    
    def test_delete_tasks(self):
        """
        Eliminar una tarea
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access)

        tasks = Tasks.objects.create(
            title='Titulo 3',
            description='Descripcion 3',
            tasks_state='',
            tasks_author=self.user
        )

        response = client.delete(
            f'/api/v1/tasks/{tasks.pk}', 
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        tasks_exists = Tasks.objects.filter(pk=tasks.pk)
        self.assertFalse(tasks_exists)


    def test_get_tasks(self):
        """
        Obtener una tarea
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access)

        Tasks.objects.create(
            title='Titulo 4',
            description='Descripcion 4',
            tasks_state='',
            tasks_author=self.user
        )

        Tasks.objects.create(
            title='Titulo 5',
            description='Descripcion 5',
            tasks_state='',
            tasks_author=self.user
        )

        response = client.get('/api/v1/tasks/')
        
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(result['count'], 2)

        for tas in result['results']:
            self.assertIn('title', tas)
            self.assertIn('description', tas)
            self.assertIn('tasks_state', tas)
            self.assertIn('tasks_author', tas)
            break


    def test_search_tasks(self):
        """
        Obtener una tarea
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access)

        Tasks.objects.create(
            title='Titulo 4',
            description='Descripcion 4',
            tasks_state='',
            tasks_author=self.user
        )

        Tasks.objects.create(
            title='Titulo 5',
            description='Descripcion 5',
            tasks_state='',
            tasks_author=self.user
        )

        response = client.get('/api/v1/tasks/?search=5')
        
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(result['count'], 1)

        for tas in result['results']:
            self.assertIn('title', tas)
            self.assertIn('description', tas)
            self.assertIn('tasks_state', tas)
            self.assertIn('tasks_author', tas)
            break
