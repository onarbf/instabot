from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace

insta_username = 'kienffuma'
insta_password = 'Q34s3rq34r4s!'

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    session.set_relationship_bounds(enabled=True,
                                     delimit_by_numbers=True,
                                      max_followers=10000,
                                      min_followers=50,
                                      min_following=50)
    session.set_simulation(enabled=True, percentage=100)
    session.set_skip_users(skip_private=False, private_percentage=0)
    session.follow_user_followers(['atractive_smithers'], amount=200, randomize=False, interact=True, sleep_delay=600)


# 'cosmeticacoreana1','sexopremarital','sntfe'
