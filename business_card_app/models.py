from django.db import models


class Footer(models.Model):
    """
    Model representing the footer section of the site.

    Attributes:
        div_text (TextField): The main text for the 'div' element (block5-text).
        p1_text (TextField): Text for the first 'p' (paragraph) element.
        p2_text (TextField): Text for the second 'p' (paragraph) element.
        p3_text (TextField): Text for the third 'p' (paragraph) element.
    """

    div_text = models.TextField(
        verbose_name="Текст для div (block5-text)",
    )
    p1_text = models.TextField(verbose_name="Текст для первого элемента p")
    p2_text = models.TextField(verbose_name="Текст для второго элемента p")
    p3_text = models.TextField(verbose_name="Текст для третьего элемента p")

    def __str__(self):
        return f"Footer ({self.id})"


class Contact(models.Model):
    """
    Model representing a contact form submission.

    Attributes:
        name (CharField): The name of the person submitting the contact form.
        number (CharField): The contact number of the person.
        comment (TextField): The comment or message from the person.
    """

    name = models.CharField(max_length=20)
    number = models.CharField(max_length=20)
    comment = models.TextField(max_length=300)

    def __str__(self):
        return self.name


class BaseGallery(models.Model):
    """
    Abstract model representing a gallery with a title, description, and images.

    Attributes:
        title (CharField): The title of the gallery.
        description (TextField): The description of the gallery.
        images (ManyToManyField): The images associated with the gallery.
    """

    title = models.CharField(
        max_length=255, verbose_name="Заголовок", default="Callery"
    )

    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    images = models.ManyToManyField("GalleryImage", verbose_name="Изображения")

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Gallery1(BaseGallery):
    """
    Model representing the first gallery, inheriting from BaseGallery.
    """

    pass


class Gallery2(BaseGallery):
    """
    Model representing the second gallery, inheriting from BaseGallery.
    """

    pass


class Gallery3(BaseGallery):
    """
    Model representing the third gallery, inheriting from BaseGallery.
    """

    pass


class Gallery4(BaseGallery):
    """
    Model representing the fourth gallery, inheriting from BaseGallery.
    """

    pass


class Gallery5(BaseGallery):
    """
    Model representing the fifth gallery, inheriting from BaseGallery.
    """

    pass


class GalleryImage(models.Model):
    """
    Model representing an individual image or video in a gallery.

    Attributes:
        image (ImageField): The image associated with the gallery.
        video_url (FileField): The video file associated with the gallery.
    """

    image = models.ImageField(
        upload_to="gallery_images/", verbose_name="Изображение", blank=True, null=True
    )
    video_url = models.FileField(
        upload_to="videos/", blank=True, null=True, verbose_name="Видео"
    )

    def __str__(self):
        image_info = f"Image: {self.image.name}" if self.image else "No Image"
        video_info = f"Video: {self.video_url.name}" if self.video_url else "No Video"
        return f"GalleryImage {self.id} - {image_info}, {video_info}"


class BiographyEvent(models.Model):
    """
    Model representing a historical event in the biography section.

    Attributes:
        year (PositiveIntegerField): The year of the event.
        text (TextField): The description of the event.
        image (ImageField): The image representing the event.
    """

    year = models.PositiveIntegerField(verbose_name="Год")
    text = models.TextField(verbose_name="Текст")
    image = models.ImageField(upload_to="biography_images/", verbose_name="Изображение")

    def __str__(self):
        return f"{self.year}: {self.text[:20]}..."


class EventBlock(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок (h5)")
    description = models.TextField(verbose_name="Описание (p)")
    title_mobile = models.CharField(
        max_length=50, default="EVENT", verbose_name="Заголовок мобильной (version)"
    )
    image = models.ImageField(
        upload_to="event_images/", verbose_name="Изображение (img)"
    )

    def __str__(self):
        return self.title


class Video(models.Model):
    """
    Model for storing videos for editing via the admin panel.
    """

    title = models.CharField(max_length=100, verbose_name="Название видео")
    video_mp4 = models.FileField(
        upload_to="videos/", verbose_name="Видео (MP4)", blank=True, null=True
    )
    video_webm = models.FileField(
        upload_to="videos/", verbose_name="Видео (WEBM)", blank=True, null=True
    )

    def __str__(self):
        return self.title
