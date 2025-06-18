from django.db import models

# Create your models here.
genres = [
    ('Action', 'Action'),('Adventure', 'Adventure'),('Animation', 'Animation'),
    ('Comedy', 'Comedy'),('Crime', 'Crime'),('Documentary', 'Documentary'),
    ('Drama', 'Drama'),('Family', 'Family'),('Fantasy', 'Fantasy'),
    ('History', 'History'),('Horror', 'Horror'),('Romance', 'Romance'),
]
languages = [
    ('English', 'English'),('Hindi', 'Hindi'),('kannada', 'Kannada'),
    ('Telugu', 'Telugu'),('Tamil', 'Tamil'),('Malayalam', 'Malayalam'),
    ('Bengali', 'Bengali'),('Punjabi', 'Punjabi'),
]

class Movie(models.Model):
    title = models.CharField(max_length=225)
    genre = models.CharField(max_length=50, choices=genres,null=True, blank=True)
    language = models.CharField(max_length=50, choices=languages,null=True, blank=True)
    synopsis = models.TextField(null=True, blank=True)
    duration_minutes = models.PositiveIntegerField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    trailer_url = models.URLField(null=True, blank=True)
    status = models.CharField(max_length=100,choices=[('Upcoming', 'Upcoming'), ('Released', 'Released')], null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    movie_image = models.ImageField(upload_to='movies/', null=True, blank=True)

    def __str__(self):
        return self.title


class Cast(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='casts')
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='casts/', null=True, blank=True)

