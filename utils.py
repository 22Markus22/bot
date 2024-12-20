from roles import Parent, Pupil
from handlers import data

def create_user (user_data: dict):
    if user_data[""]:
        if data.role == 'родитель':
            user = {'name': data.name, 'sur_name': data.sur_name, 'tel_number': data.tel_number}