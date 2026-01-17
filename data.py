import random

class Data:

    @staticmethod
    def get_name_registration():
        return 'Павел'
    
    @staticmethod
    def get_random_email():
        return f'pavelkuznetsov39{random.randint(10000, 99999)}@gmail.com'

    @staticmethod
    def get_random_password():
        return str(random.randint(100000, 999999999))

    @staticmethod
    def get_invalid_random_password():  
        return str(random.randint(0, 99999))
    
    @staticmethod
    def get_password():
        return 'tngozp33'
    
    @staticmethod
    def get_email():
        return 'pavelkuznetsov39000@gmail.com'

