from instapy import InstaPy

insta_username = 'antonpuhonin'
insta_password = 'Bulbazavr36'

try:
    session = InstaPy(username=insta_username,
                      password=insta_password,
                      headless_browser=True,
                      multi_logs=True)

    session.login()

    session.unfollow_users(amount=200, onlyInstapyFollowed = True, onlyInstapyMethod = 'FIFO', unfollow_after=4*24*60*60 )

finally:
    session.end()

