facebook_posts = [
    {'Likes':21, 'Comments':2},
    {'Likes':35, 'Comments':7, 'Shares':2},
    {'Likes':45, 'Comments':11, 'Shares':3},
    {'Comments':1, 'Shares':1},
    {'Likes':33, 'Comments':1, 'Shares':1},
]


total_likes = 0

for post in facebook_posts:
    try:
        likes = post['Likes']
    except KeyError:
        continue
    else:
        total_likes += likes
print(total_likes)