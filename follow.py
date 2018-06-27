from instapy import InstaPy

#insta_username = 'antonpuhonin'
#insta_password = 'Bulbazavr36'
insta_username = 'ira.dediaeva'
insta_password = 'kirillt123'

users_for_followers = [ 'perfume_for_the_elite', 'l.azur', 'krd_parfum', 'parfum_queens_house', 'art_selectiv_vrn', 'molecule_project', 'parfamour', 'shantual']
amount_users_by_donar = 20
amount_image_for_likes = 5

try:
    session = InstaPy(username=insta_username,
                      password=insta_password,
                      headless_browser=True,
                      multi_logs=True)

    session.login()

    session.set_user_interact(amount=amount_image_for_likes, media='Photo')
    session.set_do_follow(enabled=True, percentage=100)
    session.set_do_like(enabled=True, percentage=100)
    session.set_lower_follower_count(limit = 100)
    session.interact_user_followers(users_for_followers, amount=amount_users_by_donar, randomize=True)

finally:
    session.end()

