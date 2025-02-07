import os

URL = "http://localhost:8081/#/login"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, 'log')

if __name__ == '__main__':
    print(BASE_DIR)
    print(LOG_DIR)