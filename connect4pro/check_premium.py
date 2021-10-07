import datetime

from users.models import Connect4ProUser


def check_and_off_premium():
    users = Connect4ProUser.objects.all()
    for user in users:
        user_date = user.end_date
        now = datetime.datetime.now(user_date.tzinfo)
        if user_date <= now:
            user.is_premium = False
            user.save()


check_and_off_premium()
