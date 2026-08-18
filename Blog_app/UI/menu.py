class Menu:

    @staticmethod
    def welcome():
        print('\n-----------------BLOG APP-----------------')
        print('1.Login')
        print('2.Register')
        print('3.Exit')

    @staticmethod
    def logged_in_menu(user):
        print(f'\n--------------Welcome, {user.full_name}--------------')
        print('1.Create Post')
        print('2.List Post')
        print('3.Update Post')
        print('4.Delete Post')
        print('5.Logout')