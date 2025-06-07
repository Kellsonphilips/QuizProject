# Here we are creating a class of users like instagram users
class User:
    # this is a constructor for our objects attribute initialization
    def __init__(self, user_id, username, followers = 0, following = 0):
        self.id = user_id
        self.username = username
        self.followers = followers
        self.following = following

    # Here we can have a method to handle increment and decrement of the user followers
    def follower(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Philip",   0, 0)
user_2 = User("002", "Chigozirim", 0, 0)

# user_1 followed user_2 , so we should be able to increment user_2 followers by 1 and increment user-1 following by 1
user_1.follower(user_2)
user_2.follower(user_1) # follow back

print(user_1.id, user_1.username)
print(f"followers = {user_1.followers}", f"following = {user_1.following}")

print(user_2.id, user_2.username)
print(f"followers = {user_2.followers}", f"following = {user_2.following}")
