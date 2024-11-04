from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Commands for creating users through superuser access"

    def handle(self, *args, **options):
       
        if not User.objects.filter(username='Django').exists():
            User.objects.create_superuser(username='Django', password='django123', email='django@admin.com')
        
       
        for i in range(1, 11):
            username = f'User{i}'
            email = f'user{i}@example.com' 
            if not User.objects.filter(username=username).exists(): 
                User.objects.create_superuser(username=username, password=f'userpass{i}', email=email)
            return f'Successfully created superuser {username}'
        
        return f'User {username} already exists, skipping...'

        
#     def handle(self, *args, **options):
#         #User.objects.create_superuser(username='Django', password='django123', email='django@admin.com')
#         for i in range(1, 11):
#             User.objects.create_superuser(username=f'User{i}', password=f'userpass{i}', email=f'user{i}@example.com')

#         #return "Successfully Created "+str(User.objects.all())+"Users"
#         return "True"
        