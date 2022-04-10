# Django
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Traductor a diferentes idiomas nativo
from django.utils.translation import gettext as _ 
from django.utils import timezone

class MyUserManager(BaseUserManager):
    use_in_migrations = True
    """
    Formularios de registro de usuarios
    """
    def _create_user(self, username, password, **extra_fields):
        """
        Formulario de registro costumizado para usuarios
        """
        if not username:
            raise ValueError('EL campo username es obligatorio')

        try:
            user = self.model(username=username, **extra_fields)
        except:
            user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
  
    def create_superuser(self, username, password, **extra_fields):
        """
        Formulario de registro super usuario
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser debe tener is_superuser=True.')
        return self._create_user(username, password, **extra_fields)
    
    def create_user(self, username, password, **extra_fields):
        """
        Formulario de registro usuarios
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)

        if extra_fields.get('is_staff') is True:
            raise ValueError('Usuario debe tener is_staff=False.')
        if extra_fields.get('is_superuser') is True:
            raise ValueError('Superuser debe tener is_superuser=False.')
        return self._create_user(username, password, **extra_fields)


class TemplateUser(models.Model):

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

#########################################################################

class User(AbstractBaseUser, PermissionsMixin):
    """
    Modelo personalizado de usuarios
    """
    username = models.CharField(
        max_length=50,
        unique=True, 
        null=False,
        verbose_name=_('Username'),
        help_text=_('Usernames.'),
    )
    password = models.CharField(
        max_length=128, 
        verbose_name=_('Password'),
        help_text= _(
            "Las contraseñas sin procesar no se almacenan, por lo que no hay forma de ver la contraseña de este usuario, pero puede cambiarla utilizando <a href=\"password/\">este formulario</a>."
        ),
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designa si el usuario puede iniciar sesión en este sitio administrativo.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Indica si el usuario debe ser tratado como activo.'
            'Desmarque esta opción en lugar de borrar la cuenta.'
        ),
    )
    date_joined = models.DateTimeField(
        _('date joined'), 
        default=timezone.now
    )

    USERNAME_FIELD = 'username'
    
    objects = MyUserManager()

    def __str__(self):
        return self.username

    def get_username(self):
        return self.username

    def get_full_name(self):
        return "{} - {}".format(self.username, self.pk)

    def get_short_name(self):
        return "{}".format(self.username)

    class Meta:
        ordering = ('username',)
        verbose_name = _('Usuario')
        verbose_name_plural = _('Usuarios')
        permissions = (
            ("view_all_user", "Can view all users"),
        )
