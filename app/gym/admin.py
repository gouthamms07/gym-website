from django.contrib import admin
from .models import Booking, ContactMessage, Feature, Gallery, GymClass, Member, MembershipPlan, Service, Trainer


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "membership_plan", "status", "join_date")
    list_filter = ("status", "gender", "membership_plan")
    search_fields = ("name", "email", "phone")


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("name", "specialization", "experience", "email")
    search_fields = ("name", "specialization")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "created_at")
    search_fields = ("name",)


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "active")
    list_editable = ("order", "active")


@admin.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "duration", "active")
    list_filter = ("active",)


@admin.register(GymClass)
class GymClassAdmin(admin.ModelAdmin):
    list_display = ("name", "trainer", "day", "start_time", "capacity", "active")
    list_filter = ("active", "day")
    search_fields = ("name", "trainer__name")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("member", "gym_class", "booking_date", "status", "created_at")
    list_filter = ("status", "booking_date")
    search_fields = ("member__name", "gym_class__name")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("subject", "name", "email", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("name", "email", "subject")


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title",)
