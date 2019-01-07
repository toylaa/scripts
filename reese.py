import os
import time
from tempfile import gettempdir

from selenium.common.exceptions import NoSuchElementException

from instapy import InstaPy

insta_username = 'Reesethefrenchie_'
insta_password = 'joey54321'

# set headless_browser=True if you want to run InstaPy on a server

# set these in instapy/settings.py if you're locating the
# library in the /usr/lib/pythonX.X/ directory:
#   Settings.database_location = '/path/to/instapy.db'
#   Settings.chromedriver_location = '/path/to/chromedriver'

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  multi_logs=True)

try:
    session.login()

    #** SETTINGS **
    session.set_relationship_bounds(enabled=False,
                     #potency_ratio=-1.21,
                      delimit_by_numbers=True,
                       max_followers=4590,
                        max_following=5555,
                         min_followers=45,
                          min_following=77)
    session.set_do_follow(enabled=True, percentage=50)
    session.set_comments(["Success yo !", "Super yo !"])
    session.set_do_comment(enabled=True, percentage=80)
    session.set_do_like(True, percentage=100)
    #session.interact_by_users(['user1', 'user2', 'user3'], amount=5, randomize=True, media='Photo')
   

    #** ACTIONS **
    session.interact_by_users(['toylaa'], amount=1, randomize=False, media='Photo')

   # session.follow_by_list(followlist=['toylaa'], times=1, sleep_delay=600, interact=False)

#######################
except Exception as exc:
    # if changes to IG layout, upload the file to help us locate the change
    if isinstance(exc, NoSuchElementException):
        file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
        with open(file_path, 'wb') as fp:
            fp.write(session.browser.page_source.encode('utf8'))
        print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
            '*' * 70, file_path))
    # full stacktrace when raising Github issue
    raise

finally:
    # end the bot session
    session.end()
