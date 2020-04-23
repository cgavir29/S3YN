import os
import sys

# print(os.listdir())

def get_files(user_id):
    try:
        logs = os.listdir(f'uploaded_files/{user_id}')
        return logs
    except FileNotFoundError:
        return 'You have not uploaded any files yet.'


print(get_files('camilo'))