'''
We will learn creating classes in this section.
PascalCase: Every subscript name should be capitalized.
camelCase: Only the first letter will be in lowercase, other subscript name should be capitalized.
snake_case: All letters are lower cases, but subscript name is seperated by underscore (_).
'''


class User:
    # __func__ is called special function. Which is used for initialize attributes.
    # construction will be called automatically every time we create an object from the associate class.
    def __init__(self, id, username):  
        self.id = id
        self.username = username
        self.followers = 0  # initialized with default value
        self.following = 0  # initialized with default value

    def follow(self, user):
        user.followers +=1
        self.following +=1


user1 = User('001', 'Imran')
user2 = User('002', 'Borsha')

user1.follow(user2)

print(user1.following, user1.followers)
print(user2.following, user2.followers)


