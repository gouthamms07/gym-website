from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True


class MembershipPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2, validators=[MinValueValidator(0)])
    duration = models.PositiveIntegerField(help_text="Duration in months")
    features = models.TextField(help_text="One feature per line")
    active = models.BooleanField(default=True)
    def __str__(self): return self.name


class Member(TimestampedModel):
    class Gender(models.TextChoices):
        MALE = "male", "Male"; FEMALE = "female", "Female"; OTHER = "other", "Other"; PREFER_NOT = "prefer_not", "Prefer not to say"
    class Status(models.TextChoices):
        ACTIVE = "active", "Active"; PAUSED = "paused", "Paused"; INACTIVE = "inactive", "Inactive"
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="member_profile")
    name = models.CharField(max_length=150); email = models.EmailField(unique=True); phone = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True); gender = models.CharField(max_length=20, choices=Gender.choices, default=Gender.PREFER_NOT)
    membership_plan = models.ForeignKey(MembershipPlan, null=True, blank=True, on_delete=models.SET_NULL, related_name="members")
    join_date = models.DateField(); status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
    def __str__(self): return self.name


class Trainer(TimestampedModel):
    name = models.CharField(max_length=150); specialization = models.CharField(max_length=150); experience = models.PositiveIntegerField(help_text="Years")
    bio = models.TextField(); image = models.ImageField(upload_to="trainers/", blank=True); email = models.EmailField(); phone = models.CharField(max_length=30)
    def __str__(self): return self.name


class Service(TimestampedModel):
    name = models.CharField(max_length=150); description = models.TextField(); icon = models.CharField(max_length=80, blank=True, help_text="Icon name or emoji")
    image = models.ImageField(upload_to="services/", blank=True); price = models.DecimalField(max_digits=9, decimal_places=2, validators=[MinValueValidator(0)])
    def __str__(self): return self.name


class Feature(TimestampedModel):
    """A concise value proposition displayed on the home page."""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    icon = models.CharField(max_length=30, blank=True, help_text="Emoji or short icon identifier")
    order = models.PositiveSmallIntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ("order", "name")

    def __str__(self): return self.name


class GymClass(TimestampedModel):
    name = models.CharField(max_length=150); description = models.TextField(); trainer = models.ForeignKey(Trainer, null=True, blank=True, on_delete=models.SET_NULL, related_name="classes")
    day = models.CharField(max_length=30); start_time = models.TimeField(); end_time = models.TimeField(); capacity = models.PositiveIntegerField()
    image = models.ImageField(upload_to="classes/", blank=True); active = models.BooleanField(default=True)
    def __str__(self): return f"{self.name} — {self.day}"


class Booking(TimestampedModel):
    class Status(models.TextChoices): CONFIRMED = "confirmed", "Confirmed"; CANCELLED = "cancelled", "Cancelled"
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="bookings"); gym_class = models.ForeignKey(GymClass, on_delete=models.CASCADE, related_name="bookings")
    booking_date = models.DateField(); status = models.CharField(max_length=20, choices=Status.choices, default=Status.CONFIRMED)
    class Meta: constraints = [models.UniqueConstraint(fields=["member", "gym_class", "booking_date"], name="unique_member_class_booking")]
    def __str__(self): return f"{self.member} — {self.gym_class}"


class ContactMessage(TimestampedModel):
    class Status(models.TextChoices): NEW = "new", "New"; READ = "read", "Read"; RESOLVED = "resolved", "Resolved"
    name = models.CharField(max_length=150); email = models.EmailField(); phone = models.CharField(max_length=30, blank=True); subject = models.CharField(max_length=200); message = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    def __str__(self): return self.subject


class Gallery(TimestampedModel):
    title = models.CharField(max_length=150); image = models.ImageField(upload_to="gallery/"); description = models.TextField(blank=True)
    def __str__(self): return self.title
