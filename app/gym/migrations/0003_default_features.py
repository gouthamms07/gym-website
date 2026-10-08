from django.db import migrations


def add_default_features(apps, schema_editor):
    Feature = apps.get_model("gym", "Feature")
    features = [
        ("Modern Equipment", "Top-quality machines for every workout", "🏋", 1),
        ("Expert Trainers", "Guidance and support at every step", "♟", 2),
        ("Stronger Community", "Motivation. Support. Results.", "♥", 3),
        ("Real Results", "Transform your body and your life", "🏆", 4),
    ]
    for name, description, icon, order in features:
        Feature.objects.get_or_create(name=name, defaults={"description": description, "icon": icon, "order": order, "active": True})


def remove_default_features(apps, schema_editor):
    Feature = apps.get_model("gym", "Feature")
    Feature.objects.filter(name__in=["Modern Equipment", "Expert Trainers", "Stronger Community", "Real Results"]).delete()


class Migration(migrations.Migration):
    dependencies = [("gym", "0002_feature")]
    operations = [migrations.RunPython(add_default_features, remove_default_features)]
