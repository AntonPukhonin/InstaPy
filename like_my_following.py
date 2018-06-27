from instapy import InstaPy

insta_username = 'antonpuhonin'
insta_password = 'Bulbazavr36'

try:
    session = InstaPy(username=insta_username,
                      password=insta_password,
                      headless_browser=True,
                      multi_logs=True)
    session.login()

    session.set_user_interact(amount=5, randomize=True, percentage=50, media='Photo')
    session.set_do_like(enabled=True, percentage=70)
    session.interact_user_following([insta_username], amount=10, randomize=True)

finally:
    session.end()
