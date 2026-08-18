import mysql.connector
from repositories.user_repository import UserRepository
from repositories.blog_repository import BlogRepository
from services.authservice import AuthService
from services.blogservice import BlogService
from UI.menu import Menu
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
                elif choice=='2':
                    #register
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
        elif choice=='2':
            #list post
        elif choice=='3':
            #update()
        elif choice=='4':
            #delete
        elif choice=='5':
            self.logout()
        else:
            print('Invalid choice')       