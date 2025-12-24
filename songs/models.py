from django.db import models

class Song(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="عنوان الترنيمة"
    )

    anthropological_keywords = models.CharField(
        max_length=500,
        verbose_name="كلمات مفتاحية أنثروبولوجية",
        help_text="افصل الكلمات بفواصل"
    )

    theological_keywords = models.CharField(
        max_length=500,
        verbose_name="كلمات مفتاحية لاهوتية",
        help_text="افصل الكلمات بفواصل"
    )

    lyrics = models.TextField(
        verbose_name="كلمات الترنيمة"
    )

    powerpoint = models.FileField(
        upload_to='powerpoints/',
        verbose_name="ملف PowerPoint"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
