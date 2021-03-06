from django.core.management.base import BaseCommand, CommandError
from movies_library.models import Movie, Actor
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Generator of fake movies and actors'

    def __validated_movies_count(self, number):
        try:
            number = int(number)
        except ValueError:
            self.stdout.write('error: --movies_count argument should be integer')
        assert 0 < number <= 100, 'error: --movies_count argument should be from 1 to 100'


    def add_arguments(self, parser):
        parser.add_argument('--movies_count',
                            type=self.__validated_movies_count,
                            default=10,
                            help='The number of movies to generate')

    def handle(self, *args, **options):
        self.stdout.write('Start generating movie data')
        fake = Faker()

        for _ in range(options['movies_count']):
            movie = Movie()
            movie.title = ' '.join(fake.text().split()[:4])
            movie.year = random.randint(1996, 2021)
            movie.certificate_rate = random.choice([i[0] for i in Movie.MOVIE_CERTIFICATE])
            movie.rate = random.random() * 10
            movie.save()
            movie.actors.add(*self.__get_actors())
            self.stdout.write(f'{movie.title} movie is created')

        self.stdout.write('Data generation is finished')

    def __get_actors(self, lower_limit=1, upper_limit=20):
        actors = []
        actors_count = random.randint(lower_limit, upper_limit)
        for _ in range(actors_count):
            actor = Actor()
            actor.name = Faker().name()
            actor.save()
            actors.append(actor)
        return actors
