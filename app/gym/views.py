from django.db.models import Count
from django.shortcuts import render
from .models import Feature, GymClass, Member, Service, Trainer


def home(request):
    return render(request, "home.html", {
        "features": Feature.objects.filter(active=True)[:4],
        "services": Service.objects.order_by("name")[:3],
        "trainers": Trainer.objects.order_by("name")[:3],
        "classes": GymClass.objects.filter(active=True).select_related("trainer").order_by("day", "start_time")[:3],
        "member_count": max(100, Member.objects.filter(status=Member.Status.ACTIVE).count()),
        "class_count": max(20, GymClass.objects.filter(active=True).count()),
        "trainer_count": max(5, Trainer.objects.count()),
    })
