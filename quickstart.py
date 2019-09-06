#install instapy if neccessary, check the version of the browser and run this file with python3
# imports
from instapy import InstaPy
from instapy import smart_run
import time
# login credentials
insta_username = 'kienffuma'
insta_password = 'Q34s3rq34r4s!'

comments = ['Nice shot! @{}',
        'I love your profile! @{}',
        'Your feed is an inspiration :thumbsup:',
        'Just incredible :open_mouth:',
        'What camera did you use @{}?',
        'Love your posts @{}',
        'Looks awesome @{}',
        'Getting inspired by you @{}',
        ':raised_hands: Yes!',
        'I can feel your passion @{} :muscle:',
        'go go go!']
# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
  """ Activity flow """
  # general settings
  session.set_do_like(enabled=True, percentage=70)
  session.set_relationship_bounds(enabled=True,
                                   delimit_by_numbers=True,
                                    max_followers=2500,
                                    min_followers=50,
                                    max_following=2500,
                                    min_following=50,
                                    potency_ratio=-0.3 #max relationship_ratio
                                    )

  session.set_simulation(enabled=True, percentage=100)
  session.set_skip_users(skip_private=False, private_percentage=0)
  # activity
  session.follow_user_followers(['cosmeticacoreana1', ], amount=300, randomize=True,interact=True, sleep_delay=60)

  # Joining Engagement Pods
  session.set_do_comment(enabled=True, percentage=35)
  session.set_comments(comments)
  session.join_pods()
