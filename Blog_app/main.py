import mysql.connector
from Repositories.blog_repository import BlogRepository
from Repositories.user_repository import UserRepository
from Services.auth_service import AuthService
from Services.blog_service import BlogService
from UI.menu import Menu
from Utils.validators import validate_required, validate_user_id


class BlogApp:
    def __init__(self):
        self.auth_service=AuthService(UserRepository())
        self.blog_service=BlogService(BlogRepository())
        self.current_user=None

    def run(self):
        while True:
            if self.current_user is None:
                Menu.welcome()
                choice=input('Enter your choice: ')
                if choice=='1':
                    #login
                    self.login()

                elif choice=='2':
                    #register
                    self.register()

                elif choice=='3':
                    print('GoodBYE!')
                    break
                else:
                    print('Invalid choice')
            else:
                self.logged_in_menu()
    def register(self):
        print('---------------------REGISTER---------------------')
        user_id=input('Enter user ID: ')
        valid,message=validate_user_id(user_id)
        if not valid:
            print(message)
            return

        password=input('Enter password: ')
        valid,message=validate_required(password,"Password")
        if not valid:
            print(message)
            return

        first_name=input('Enter firstname: ')
        valid,message=validate_required(first_name,"First Name")
        if not valid:
            print(message)
            return

        last_name=input('Enter last name: ')
        valid,message=validate_required(last_name,"Last Name")

        if not valid:
            print(message)
            return

        try:
            success,message=self.auth_service.register(
                user_id.strip(),
                password,
                first_name.strip(),
                last_name.strip()
            )
            print(message)
        except mysql.connector.Error as e:
            print('Database operation failed: ',e)

    def login(self):
        print('\n----------------LOGIN----------------')
        user_id=input('Enter User ID: ')
        password=input('Enter password: ')
        if not user_id or not password:
            print('Useer ID and password cannot be blank')
        try:
            user=self.auth_service.login(user_id,password)
            if user:
                self.current_user=user
                print(f"Login successful. Welcome, {user.full_name}")
            else:
                print('Invalid User ID or Password')

        except mysql.connector.Error as e:
            print('Database operation failed: ',e)

    def logged_in_menu(self):
        Menu.logged_in_menu(self.current_user)
        choice=input('Enter your choice: ')

        if choice=='1':
            #create post
            self.create_post()

        elif choice=='2':
            #list post
            self.list_post()

        elif choice=='3':
            #update()
            self.update_post()

        elif choice=='4':
            #delete
            self.delete_post()

        elif choice=='5':
            self.logout()
            
        else:
            print('Invalid choice')       


    def create_post(self):
        print("\n----------CREATE POST-----------\n")

        title = input("Enter Title: ")
        valid, message = validate_required(title,"Title")
        if not valid:
            print(message)
            return
        description = input("Enter description: ")
        valid, message = validate_required(description,"Description")
        if not valid:
            print(message)
            return

        try:
            self.blog_service.create_post(
                self.current_user,
                title.strip(),
                description.strip()
            )
            print("Post Created Successfully.")
        except mysql.connector.Error as e:
            print("Database operation failed: ",e)

    def list_post(self):
        print("\n---------------RECENT POST------------\n")
        try:
            posts = self.blog_service.list_posts()

            if not posts:
                print("No post available.")
                return
            for post in posts:
                print("\n-------------------------")
                print("Blog ID: ",post["blog_id"])
                print("Author: ", post["author_name"])
                print("Title: ", post["title"])
                print("Description: ", post["description"])
                print("Posted: ", post["created_at"])
        except mysql.connector.connect as e:
            print("Database operation failed: ",e)

    def update_post(self):
        print("\n--------------UPDATE POST-----------")
        try:
            blog_id = int(input("Enter Blog ID: "))
        except ValueError:
            print("Blog ID must be a number")
            return
        title = input("Enter the new Title: ")
        valid, message  = validate_required(title,"title")
        if not valid:
            print(message)
            return
        description = input("Enter the new description: ")
        valid, message  = validate_required(description,"Description")
        if not valid:
            print(message)
            return
        try:
            updated = self.blog_service.update_post(
                self.current_user,
                blog_id,
                title.strip(),
                description.strip()
            )
            if updated:
                print("Post updated Successfully")
            else:
                print("Post not found or you are not the owner of this post")
        except mysql.connector.Error as e:
            print("Database operation failed: ", e)

    def delete_post(self):
        print("\n----------DELETE POST-------------")

        try:
            blog_id = int(input("Enter the Blog ID: "))
        except ValueError:
            print("Blog ID must be a number.")
            return

        try:
            deleted = self.blog_service.delete_post(
                self.current_user,
                blog_id
            )
            if deleted:
                print("Post deleted Succesfully.")
            else:
                print("Post not found or you are not the owner of this post")

        except mysql.connector.Error as e:
            print("Database operation failed: ",e)

    def logout(self):
        self.current_user = None
        print("Logged out successfully")

if __name__ == "__main__":
    app = BlogApp()
    app.run()