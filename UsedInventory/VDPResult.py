import json
import unittest
import requests

class VDPResult(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('config.json') as config_file:
            cls.config = json.load(config_file)

    def test_dealRatings_by_channel_get(self):
        """Test to get  response."""
        # Perform a GET request
        for case in self.config['DealerList']:
            with self.subTest(dealerID=case['dealerID']):
                response = requests.get(f"{self.config['BASE_URL']}/api/v2/reports/recent-activity-report-dol?dol_max=2000&dol_min=0&date_from=2021-01-01&date_to=2024-11-01&dealership_uid={case['dealerID']}&page=1&page_size=10&ordering=-vdps&search=&inventory=used", headers={"Authorization": f"Bearer {self.config['manual_token']}"})
                print("Dealer Name: ", case['DealerName'])
                print("Response Status Code: ", response.status_code)
                print("Response: ", response.json(), "\n")
                self.assertEqual(response.status_code, 200)
                self.assertGreater(len(response.json()), 0)