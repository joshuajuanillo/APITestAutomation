import json
import unittest
import requests

class MarketingResult(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('config.json') as config_file:
            cls.config = json.load(config_file)

    def test_budget_roi_get(self):
        """Test to get VDPS response."""
        # Perform a GET request
        for case in self.config['DealerList']:
            with self.subTest(dealerID=case['dealerID']):
                response = requests.get(f"{self.config['BASE_URL']}/api/v2/sales/budget-roi?date_from=2024-08-04&date_to=2024-11-01&dealership_uid={case['dealerID']}&inventory=used", headers={"Authorization": f"Bearer {self.config['manual_token']}"})
                print("Dealer Name: ", case['DealerName'])
                print("Response Status Code: ", response.status_code)
                print("Response: ", response.json(), "\n")
                self.assertEqual(response.status_code, 200)
                self.assertGreater(len(response.json()), 0)

    def test_vdps_by_channel_get(self):
        """Test to get VDPS response."""
        # Perform a GET request
        for case in self.config['DealerList']:
            with self.subTest(dealerID=case['dealerID']):
                response = requests.get(f"{self.config['BASE_URL']}/api/v2/sales/vdps-by-channel?date_from=2024-09-10&date_to=2024-09-16&dealership_uid={case['dealerID']}&inventory=used", headers={"Authorization": f"Bearer {self.config['manual_token']}"})
                print("Dealer Name: ", case['DealerName'])
                print("Response Status Code: ", response.status_code)
                print("Response: ", response.json(), "\n")
                self.assertEqual(response.status_code, 200)
                self.assertGreater(len(response.json()), 0)

    def test_top_10_website_get(self):
        """Test to get VDPS response."""
        # Perform a GET request
        for case in self.config['DealerList']:
            with self.subTest(dealerID=case['dealerID']):
                response = requests.get(f"{self.config['BASE_URL']}/api/v2/sales/top-ten-website-sources?date_from=2024-09-10&date_to=2024-09-16&dealership_uid={case['dealerID']}&inventory=used", headers={"Authorization": f"Bearer {self.config['manual_token']}"})
                print("Dealer Name: ", case['DealerName'])
                print("Response Status Code: ", response.status_code)
                print("Response: ", response.json(), "\n")
                self.assertEqual(response.status_code, 200)
                self.assertGreater(len(response.json()), 0)

    def test_vdp_roi_get(self):
        """Test to get VDPS response."""
        # Perform a GET request
        for case in self.config['DealerList']:
            with self.subTest(dealerID=case['dealerID']):
                response = requests.get(f"{self.config['BASE_URL']}/api/sales/v2/vdp-roi?date_from=2024-06-19&date_to=2024-09-16&dealership_uid={case['dealerID']}&source_type=website&inventory=used", headers={"Authorization": f"Bearer {self.config['manual_token']}"})
                print("Dealer Name: ", case['DealerName'])
                print("Response Status Code: ", response.status_code)
                print("Response: ", response.json(), "\n")
                self.assertEqual(response.status_code, 200)
                self.assertGreater(len(response.json()), 0)