from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager



class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError("The Email must be set")

        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    email = models.EmailField(
        verbose_name=_("email"),
        unique=True,
        blank=False,
        null=False
    )

    first_name = models.CharField(
        verbose_name=_("first name"),
        max_length=256,
        blank=True,
        null=False,
        default=""
    )

    last_name = models.CharField(
        verbose_name=_("last name"),
        max_length=256,
        blank=True,
        null=False,
        default=""
    )

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(default=timezone.now)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    def __str__(self):
        return self.email

    @property
    def news_count(self):
        return self.news.count



class New(models.Model):

    class Meta:
        verbose_name = _("New")
        verbose_name_plural = _("News")

    MAX_LENGTH = 100

    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("inprogress", "In Progress"),
        ("published", "Published")
    )

    title = models.CharField(
        verbose_name=_("title"),
        max_length=MAX_LENGTH,
        blank=False,
        null=False
    )

    author = models.CharField(
        verbose_name=_("author"),
        max_length=MAX_LENGTH,
        blank=False,
        null=False,
        default=""
    )

    """
        Links
    """
    facebook_link = models.URLField(
        verbose_name=_("facebook link"),
        blank=True,
        null=False
    )

    twitter_link = models.URLField(
        verbose_name=_("twitter link"),
        blank=True,
        null=False
    )

    linkedin_link = models.URLField(
        verbose_name=_("linkedin link"),
        blank=True,
        null=False
    )


    content = models.TextField(
        verbose_name=_("content"),
        blank=True,
        null=False,
        default=""
    )


    status = models.CharField(
        verbose_name=_("status"),
        max_length=20,
        choices=STATUS_CHOICES,
        default="Draft",
        blank=False,
        null=False
    )

    created_at = models.DateTimeField(verbose_name=_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("updated at"), auto_now=True)

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("creator"), on_delete=models.CASCADE, related_name="news")


    def __str__(self):
        return self.title
