import json
import unittest

from flask_jwt_extended import create_refresh_token

from tests.mixins import ResourceTestsMixin


class AuthResourceTests(ResourceTestsMixin, unittest.TestCase):
    def test_user_sign_in(self):
        user, _ = self.create_user()
        data = json.dumps({
            'username': 'testuser',
            'password': 'password',
        })
        response = self.client.post(
            '/api/auth/token', follow_redirects=True, data=data
        )
        self.assertEqual(response.status_code, 200)

    def test_token_refresh(self):
        user, _ = self.create_user()
        with self.context:
            refresh_token = create_refresh_token(user.id)
        headers = {'Authorization': 'Bearer ' + refresh_token}
        response = self.client.post(
            '/api/auth/refresh', follow_redirects=True, headers=headers
        )
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
