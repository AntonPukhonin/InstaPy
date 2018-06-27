from instapy import InstaPy

#insta_username = 'antonpuhonin'
#insta_password = 'Bulbazavr36'
insta_username = 'tonparfums'
insta_password = 'ov9AN6NlnV'

try:
    session = InstaPy(username=insta_username,
                      password=insta_password,
                      headless_browser=True,
                      multi_logs=True)

    session.login()

    session.unfollow_users(amount=200, onlyInstapyFollowed = False, onlyInstapyMethod = 'FIFO', unfollow_after=1*12*60*60 )

finally:
    session.end()

