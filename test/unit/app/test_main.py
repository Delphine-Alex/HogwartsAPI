import unittest
import requests

url = 'http://127.0.0.1:8000'

class TestMain(unittest.TestCase):
    def setUp(self):
        self.wizard_data = {
            "firstname": "Test",
            "lastname": "Test",
            "house": "Test"
        }

    def test_00_add_wizard(self):
        response = requests.post(url + '/wizards', json=self.wizard_data)
        self.assertEqual(response.status_code, 200)
        wizard = response.json()
        self.assertEqual(wizard['firstname'], self.wizard_data['firstname'])
        self.assertEqual(wizard['lastname'], self.wizard_data['lastname'])
        self.assertEqual(wizard['house'], self.wizard_data['house'])


    def test_01_update_wizard_by_id(self):
        response = requests.get(url + '/wizards')
        wizard = response.json()
        for i in range(0, len(wizard["data"])):
            if wizard["data"][i]["firstname"] == "Test":
                id_wizard = wizard["data"][i]["id"]
                break

        updated_wizard_data = {
        "firstname": "Test01",
        "lastname": "Test01",
        "house": "Test01"
        }

        response = requests.put(url + f'/wizards/{id_wizard}', json=updated_wizard_data)
        self.assertEqual(response.status_code, 200)
        updated_wizard = response.json()
        
        self.assertEqual(updated_wizard['firstname'], updated_wizard_data['firstname'])
        self.assertEqual(updated_wizard['lastname'], updated_wizard_data['lastname'])
        self.assertEqual(updated_wizard['house'], updated_wizard_data['house'])


    def test_03_delete_wizard_by_id(self):
        response = requests.get(url + '/wizards')
        wizard = response.json()
        for i in range(0, len(wizard["data"])):
            if wizard["data"][i]["firstname"] == "Test01":
                id_wizard = wizard["data"][i]["id"]
                break

        response = requests.delete(url + f'/wizards/{id_wizard}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
