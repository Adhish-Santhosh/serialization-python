from django.db import models


class Questions(models.Model):

    title = models.CharField(max_length=200)

    Language_Choices = (
        ("python", "python"),
        ("java", "java"),
        ("javascript", "javascript"),
        ("c", "c"),
    )

    language = models.CharField(
        max_length=200,
        choices=Language_Choices,
        default="python"
    )

    Difficulty_level = (
        ("easy", "easy"),
        ("medium", "medium"),
        ("Hard", "Hard"),
    )

    difficulty_level = models.CharField(
        max_length=200,
        choices=Difficulty_level,
        default="easy"
    )

    notes = models.TextField(null=True)

    topic = models.CharField(max_length=200)

    published_date = models.DateTimeField(
        auto_now_add=True
    )
    sample_input=models.TextField()

    sample_output = models.TextField()

    is_active = models.BooleanField(default=True) 