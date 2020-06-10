
from flask_jwt_extended import create_access_token

from find_it import create_app, db
from find_it.models import User


class ResourceTestsMixin:
    def create_user(self, admin=False):
        with self.context:
            user = User(username='testuser')
            user.password = 'password'
            if admin:
                user.is_admin = True
            db.session.add(user)
            db.session.commit()
            return user, create_access_token(user.id)

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.context = self.app.app_context()
        with self.context:
            db.create_all()

    def tearDown(self):
        with self.context:
            db.session.remove()
            db.drop_all()
