class User:
    def __init__(self, username):
        self.username = username
        self.posts = []
        self.following = []

    def add_post(self, post):
        self.posts.append(post)

    def follow(self, user):
        if user not in self.following:
            self.following.append(user)
            print(f"{self.username} is now following {user.username}.")
        else:
            print(f"{self.username} is already following {user.username}.")

    def view_posts(self):
        print(f"\nPosts by {self.username}:")
        if not self.posts:
            print("No posts yet.")
        for post in self.posts:
            print(f"- {post}")

class SocialMedia:
    def __init__(self):
        self.users = {}

    def create_user(self, username):
        if username not in self.users:
            self.users[username] = User(username)
            print(f"User '{username}' created.")
        else:
            print(f"Username '{username}' is already taken.")

    def post_message(self, username, message):
        if username in self.users:
            self.users[username].add_post(message)
            print(f"{username} posted: {message}")
        else:
            print(f"User '{username}' does not exist.")

    def follow_user(self, follower, followee):
        if follower in self.users and followee in self.users:
            self.users[follower].follow(self.users[followee])
        else:
            print("One or both users do not exist.")

    def view_user_posts(self, username):
        if username in self.users:
            self.users[username].view_posts()
        else:
            print(f"User '{username}' does not exist.")

def main():
    platform = SocialMedia()

    while True:
        print("\nSocial Media Platform")
        print("1. Create User")
        print("2. Post Message")
        print("3. Follow User")
        print("4. View User Posts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter a username: ")
            platform.create_user(username)

        elif choice == '2':
            username = input("Enter your username: ")
            message = input("Enter your message: ")
            platform.post_message(username, message)

        elif choice == '3':
            follower = input("Enter your username: ")
            followee = input("Enter the username to follow: ")
            platform.follow_user(follower, followee)

        elif choice == '4':
            username = input("Enter the username to view posts: ")
            platform.view_user_posts(username)

        elif choice == '5':
            print("Exiting the platform.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
