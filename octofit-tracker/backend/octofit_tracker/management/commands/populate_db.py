from django.core.management.base import BaseCommand
from octofit_tracker.test_data import create_test_data

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts.'

    def handle(self, *args, **kwargs):
        create_test_data()
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
