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
    

    def test00_read_main(self):
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

    # Check endpoint: add a wizard to the database
    def test_01_add_wizard(self):
        response = requests.post(url + '/wizards', json=self.wizard_data)
        self.assertEqual(response.status_code, 200)
        wizard = response.json()
        self.assertEqual(wizard['firstname'], self.wizard_data['firstname'])
        self.assertEqual(wizard['lastname'], self.wizard_data['lastname'])
        self.assertEqual(wizard['house'], self.wizard_data['house'])


    # Check endpoint: update a existing wizard
    def test_02_update_wizard_by_id(self):
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


    # Check endpoint: get the list of wizard
    def test_03_get_wizards(self):
        response = requests.get(url + '/wizards')
        self.assertEqual(response.status_code, 200)
        wizards = response.json()["data"]
        self.assertIsInstance(wizards, list)
        self.assertGreater(len(wizards), 0)
        wizard = wizards[0]
        self.assertIsInstance(wizard, dict)
        self.assertIn("id", wizard)
        self.assertIsInstance(wizard["id"], int)
        self.assertIn("firstname", wizard)
        self.assertIsInstance(wizard["firstname"], str)
        self.assertIn("lastname", wizard)
        self.assertIsInstance(wizard["lastname"], str)
        self.assertIn("house", wizard)
        self.assertIsInstance(wizard["house"], str)


    # Check endpoint: get of a particular wizard
    def test_04_get_wizard_by_id(self):
        response = requests.get(url + '/wizards')
        wizard = response.json()
        for i in range(0, len(wizard["data"])):
            if wizard["data"][i]["firstname"] == "Test01":
                id_wizard = wizard["data"][i]["id"]
                break

        response = requests.get(url + f'/wizards/{id_wizard}')
        self.assertEqual(response.status_code, 200)
        wizard = response.json()
        self.assertIsInstance(wizard, dict)
        self.assertIn("id", wizard)
        self.assertIsInstance(wizard["id"], int)
        self.assertIn("firstname", wizard)
        self.assertIsInstance(wizard["firstname"], str)
        self.assertIn("lastname", wizard)
        self.assertIsInstance(wizard["lastname"], str)
        self.assertIn("house", wizard)
        self.assertIsInstance(wizard["house"], str)


    # Check endpoint: delete a wizard from the database
    def test_05_delete_wizard_by_id(self):
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
