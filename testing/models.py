from django.db import models



class Testing(models.Model):
    title = models.CharField(max_length=255)
    test_description = models.TextField(blank=True, default='')

    def __str__(self):
        return '{}: {}'.format(self.title, self.test_description)
