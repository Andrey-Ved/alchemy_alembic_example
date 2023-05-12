from app.db.db import DataBase
from app.data import users


def main():
    base = DataBase()

    base.clear_db()

    users_id = []
    for user in users:
        users_id.append(
            base.create(user)
        )

    for user_id in users_id:
        print(
            base.read(user_id)
        )


if __name__ == '__main__':
    main()
