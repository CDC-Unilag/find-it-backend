import json
import unittest

from tests.mixins import ResourceTestsMixin


class V1ResourceTests(ResourceTestsMixin, unittest.TestCase):
    def test_root(self):
        response = self.client.get('/api/v1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_user_sign_up(self):
        data = json.dumps({
            'username': 'testuser',
            'password': 'password',
            'confirm_password': 'password',
        })
        response = self.client.post(
            '/api/v1/user', follow_redirects=True, data=data
        )
        self.assertEqual(response.status_code, 201)

    def test_admin_get_users(self):
        user, access_token = self.create_user(admin=True)
        headers = {'Authorization': 'Bearer ' + access_token}
        response = self.client.get(
            'api/v1/user', follow_redirects=True, headers=headers
        )
        self.assertEqual(response.status_code, 200)

    def test_non_admin_get_users(self):
        user, access_token = self.create_user()
        headers = {'Authorization': 'Bearer ' + access_token}
        response = self.client.get(
            'api/v1/user', follow_redirects=True, headers=headers
        )
        self.assertEqual(response.status_code, 403)

    def test_get_leaderboard(self):
        response = self.client.get(
            'api/v1/leaderboard', follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
