from io import BytesIO
import uuid
import qrcode
from django.db import models
from django.utils.text import slugify
from account.models import User
from ..event_category.models import EventCategory
import os
import cloudinary
import cloudinary.uploader

class Event(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    image = models.ImageField(upload_to='events-api/events/') 
    location = models.CharField(max_length=2000)
    description = models.TextField()
    ticket_price = models.CharField(max_length=100)
    tickets_available = models.PositiveIntegerField()
    is_cancelled = models.BooleanField(default=False)
    category = models.ManyToManyField(EventCategory, related_name='eventscategory')
    qr_code = models.CharField(max_length=255, unique=True, editable=False)  # Making it non-editable
    custom_link = models.CharField(max_length=255, help_text='Choose a memorable link name, e.g. mywedding, giftbirthday')
# 'organizer', 'name', 'date_time', 'location', 'description', 'ticket_price', 'tickets_available', 'is_cancelled', 'category', 'qr_code', 'custom_links'
    def __str__(self):
        return self.name


    def generate_unique_qr_code(self):
        unique_identifier = uuid.uuid4().hex
        data = f"Unique ID: {unique_identifier}\nEvent ID: {self.id}\nEvent: {self.name}\nOrganizer: {self.organizer.email}"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img_io = BytesIO()
        img.save(img_io, format='PNG')
        img_io.seek(0)

        # Upload the image to Cloudinary
        response = cloudinary.uploader.upload(
            img_io,
            public_id=f'events-api/qr_codes/event_{self.id}',
            api_key=os.getenv('CLOUDINARY_API_KEY'),
            api_secret=os.getenv('CLOUDINARY_API_SECRET'),
            cloud_name=os.getenv('CLOUD_NAME')
        )

        # Get the Cloudinary URL from the response
        cloudinary_url = response['secure_url']

        return cloudinary_url

    def save(self, *args, **kwargs):
        if not self.qr_code:
            self.qr_code = self.generate_unique_qr_code()
        super().save(*args, **kwargs)
