from datetime import datetime


users = [
    {
        'name': 'Петя',
        'birth_date': datetime.strptime('2023-01-01', '%Y-%m-%d').date(),
        'gender': 'male'
    },
    {
        'name': 'Вася',
        'birth_date': datetime.strptime('2022-01-01', '%Y-%m-%d').date(),
        'gender': 'male'
    },
    {
        'name': 'Маша',
        'birth_date': datetime.strptime('2021-01-01', '%Y-%m-%d').date(),
        'gender': 'female'
    },
]