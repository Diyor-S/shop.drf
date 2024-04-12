from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.db.models import CharField
from django.utils.translation import gettext_lazy as _


class Media(models.Model):
    class FileType(models.TextChoices):
        IMAGE = 'image', _("Image")
        VIDEO = 'video', _("Video")
        DOCUMENT = 'document', _("Document")
        GIF = 'gif', _("Gif")
        OTHER = 'other', _("Other")

    file = models.FileField(upload_to='medias',
                            verbose_name=_("File"),
                            validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png', 'webp',
                                                                                   'mp4', 'avi', 'mpeg4', 'mkv',
                                                                                   'pdf', 'doc', 'docx',
                                                                                   'gif'])])

    file_type = models.CharField(max_length=20,
                                 verbose_name=_("File Type"),
                                 choices=FileType.choices)

    def clean(self):
        if self.file_type not in self.FileType.values:
            raise ValidationError(_("Invalid File Type"))
        elif self.file_type == self.FileType.IMAGE:
            if self.file.name.split('.')[-1] not in ['jpeg', 'jpg', 'png', 'webp']:
                raise ValidationError(_("Invalid Image File"))
        elif self.file_type == self.FileType.VIDEO:
            if self.file.name.split('.')[-1] not in ['avi', 'mkv', 'mov', 'mp4']:
                raise ValidationError(_("Invalid Video File"))
        elif self.file_type == self.FileType.DOCUMENT:
            if self.file.name.split('.')[-1] not in ['doc', 'docx', 'pdf']:
                raise ValidationError(_("Invalid Document File"))

    class Meta:
        verbose_name = _("Media")
        verbose_name_plural = _("Media")

    def __str__(self):
        return f"Id: {self.id} | Name: {self.file.name.split('/')[-1]}"


class CommonSettings(models.Model):
    main_phone_number = models.CharField(_("Main Phone Number"), max_length=20)
    main_address = models.CharField(_("Main Address"), max_length=100)
    main_email_address = models.EmailField(_("Main Email Address"))
    main_home_greeting_text = models.TextField(_("Main Home Greeting Text"))
    main_home_greeting_image = models.ForeignKey(Media,
                                                 on_delete=models.CASCADE,
                                                 verbose_name=_("Main Home Greeting Image"),
                                                 related_name="main_home_greeting_image")
    our_blog_page_back_image = models.ForeignKey(Media,
                                                 on_delete=models.CASCADE,
                                                 verbose_name=_("Our Blog Page Back Image"),
                                                 related_name="our_blog_page_back_image")
    you_may_be_interested_in_page_back_image = models.ForeignKey(Media,
                                                                 on_delete=models.CASCADE,
                                                                 verbose_name=_("You May Be Interested In Page Back "
                                                                                "Image"),
                                                                 related_name="you_may_be_interested_in_page_back_image")
    related_products_back_image = models.ForeignKey(Media,
                                                    on_delete=models.CASCADE,
                                                    verbose_name=_("Related Products Back Image"),
                                                    related_name="related_products_back_image")

    def __str__(self):
        return self.main_phone_number

    class Meta:
        verbose_name = _("Common Settings")
        verbose_name_plural = _("Common Settings")

