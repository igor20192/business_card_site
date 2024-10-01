from django.db import models


class Footer(models.Model):
    div_text = models.TextField(verbose_name="Текст для div (block5-text)")
    p1_text = models.TextField(verbose_name="Текст для первого элемента p")
    p2_text = models.TextField(verbose_name="Текст для второго элемента p")
    p3_text = models.TextField(verbose_name="Текст для третьего элемента p")

    def __str__(self):
        return f"Footer ({self.id})"


class Contact(models.Model):
    name = models.CharField(max_length=20)
    number = models.CharField(max_length=20)
    comment = models.TextField(max_length=300)

    def __str__(self):
        return self.name


class BaseGallery(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    images = models.ManyToManyField("GalleryImage", verbose_name="Изображения")

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Gallery1(BaseGallery):
    pass


class Gallery2(BaseGallery):
    pass


class Gallery3(BaseGallery):
    pass


class Gallery4(BaseGallery):
    pass


class Gallery5(BaseGallery):
    pass


class GalleryImage(models.Model):
    image = models.ImageField(
        upload_to="gallery_images/", verbose_name="Изображение", blank=True, null=True
    )
    video_url = models.FileField(
        upload_to="videos/", blank=True, null=True, verbose_name="Видео"
    )

    def __str__(self):
        return f"Image {self.id}"


class BiographyEvent(models.Model):
    year = models.PositiveIntegerField(verbose_name="Год")
    text = models.TextField(verbose_name="Текст")
    image = models.ImageField(upload_to="biography_images/", verbose_name="Изображение")

    def __str__(self):
        return f"{self.year}: {self.text[:20]}..."
