from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams

        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create Users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team='Marvel')
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team='Marvel')
        batman = User.objects.create(name='Batman', email='batman@dc.com', team='DC')
        superman = User.objects.create(name='Superman', email='superman@dc.com', team='DC')

        # Create Activities
        from datetime import date
        Activity.objects.create(user=ironman, activity_type='Run', duration=30, date=date.today())
        Activity.objects.create(user=batman, activity_type='Swim', duration=45, date=date.today())
        Activity.objects.create(user=superman, activity_type='Cycle', duration=60, date=date.today())
        Activity.objects.create(user=captain, activity_type='Walk', duration=20, date=date.today())

        # Create Workouts
        Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', suggested_for='All')
        Workout.objects.create(name='Strength Training', description='Strength for DC', suggested_for='DC')
        Workout.objects.create(name='Agility Drills', description='Agility for Marvel', suggested_for='Marvel')

        # Create Leaderboard
        Leaderboard.objects.create(user=ironman, points=100)
        Leaderboard.objects.create(user=batman, points=90)
        Leaderboard.objects.create(user=superman, points=95)
        Leaderboard.objects.create(user=captain, points=85)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
