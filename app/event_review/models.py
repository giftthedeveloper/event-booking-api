from django.db import models
from ..events.events_models import Event
from account.models import User

class EventReview(models.Model):
    """ review model to handle event reviews from both anonymous and organiser users """
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    # reviewer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=1000)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 5)])
    review_text = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'review by {self.name} on {self.event.name}'