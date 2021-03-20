from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Logo(models.Model):
    # file will be uploaded to MEDIA_ROOT / uploads
    logo = models.FileField(upload_to="uploads/")


class TimeStampedModel(models.Model):
    """TimeStampedModel.
    An abstract base class model that provides self-managed "created" and
    "updated" fields.
    """

    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_on = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        get_latest_by = 'modified_on'
        ordering = ('-modified_on', '-created_on',)
        abstract = True


class Service(models.Model):
    """Service model."""
    topic = models.CharField(max_length=50, null=True, blank=True)
    discription = RichTextUploadingField(null=True, blank=True)
    summary = RichTextUploadingField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name_plural = "Service"


class ContactUs(TimeStampedModel):
    """ContactUs model."""

    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=254, null=True, blank=True)
    address = models.CharField(max_length=254, null=True, blank=True)
    message = RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Us"


class AboutUs(TimeStampedModel):
    """AboutUs model."""

    topic = models.CharField(max_length=255, null=True, blank=True)
    discription = RichTextUploadingField(null=True, blank=True)
    discription2 = RichTextUploadingField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name_plural = "About Us"


class WhyUs(models.Model):
    """WhyUs model."""

    topic = models.CharField(max_length=255, null=True, blank=True)
    discription = RichTextUploadingField(null=True, blank=True)
    discription2 = RichTextUploadingField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name_plural = "Why Choose Us"



class Settings(models.Model):
    """Settings model."""
    facebook = models.CharField(max_length=50, null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)
    twitter = models.CharField(max_length=50, null=True, blank=True)
    youtube = models.CharField(max_length=50, null=True, blank=True)
    

    def __str__(self):
        return self.facebook

    class Meta:
        verbose_name_plural = "Settings"


class Slider(TimeStampedModel):
    """Slider model."""

    topic = models.CharField(max_length=50, null=True, blank=True)
    sub_topic = models.CharField(max_length=50, null=True, blank=True)
    discription = RichTextUploadingField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name_plural = "Slider"


class Enquiry(models.Model):
    """Enquiry model."""
    PRODUCT_CHOICES =( 
        ("led", "LED TV"),
        ("lcd", "LCD TV"),
        ("plasma", "PLASMA TV"),
    )
    BRAND_CHOICES =( 
        ("Akai", "Akai"),
        ("Aiwa", "Aiwa"),
        ("BPL", "BPL"),
        ("Daewoo", "Daewoo"),
        ("Haier", "Haier"),
        ("Hyundai", "Hyundai"),
        ("Hitachi", "Hitachi"),
        ("Koryo", "Koryo"),
        ("LG", "LG"),
        ("Lyod", "Lyod"),
        ("Mitsubishi", "Mitsubishi"),
        ("Onida", "Onida"),
        ("Philips", "Philips"),
        ("Panasonic", "Panasonic"),
        ("Pioneer", "Pioneer"),
        ("Sanyo", "Sanyo"),
        ("Sharp", "Sharp"),
        ("Samsung", "Samsung"),
        ("Sansui", "Sansui"),
        ("Toshiba", "Toshiba"),
        ("Thomson", "Thomson"),
        ("Texla", "Texla"),
        ("Videocon", "Videocon"),
        ("IMPORTED Product", "IMPORTED Product"),
        ("Other COMPANY/BRAND", "Other COMPANY/BRAND")
    )
    SERVICES_CHOICES =( 
        ("Repairing", "Repairing"),
        ("Installation", "Installation")
    )
    name = models.CharField(max_length=50, null=True, blank=True)
    contact_no = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=254, null=True, blank=True)
    product = models.CharField(choices=PRODUCT_CHOICES, max_length=200, null=True, blank=True)
    brand = models.CharField(choices=BRAND_CHOICES, max_length=200, null=True, blank=True)
    service = models.CharField(choices=SERVICES_CHOICES, max_length=200, null=True, blank=True)
    message = RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name_plural = "Enquiry"
