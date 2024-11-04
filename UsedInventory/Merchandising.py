import json
import unittest
import requests

class Merchandising(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('config.json') as config_file:
            cls.config = json.load(config_file)

    def test_dealRatings_by_channel_get(self):
        """Test to get response."""
        # Perform a GET request
        for case in self.config['DealerList']:
            with self.subTest(dealerID=case['dealerID']):
                response = requests.get(f"{self.config['BASE_URL']}/api/sales/v2/deal-ratings?date_from=2024-10-25&date_to=2024-10-31&dealership_uid={case['dealerID']}&page=1&page_size=10&ordering=-stock_number&search=&source=ATC&source=CGR&inventory=used", headers={"Authorization": f"Bearer {self.config['manual_token']}"})
                print("Dealer Name: ", case['DealerName'])
                print("Response Status Code: ", response.status_code)
                print("Response: ", response.json() , "\n")
                self.assertEqual(response.status_code, 200)
                self.assertGreater(len(response.json()), 0)

    def test_tip_report_get(self):
        """Test to get response."""
        # Perform a GET request
        for case in self.config['DealerList']:
            with self.subTest(dealerID=case['dealerID']):
                response = requests.get(f"{self.config['BASE_URL']}/api/v2/sales/tip-report?date_from=2024-10-26&date_to=2024-11-01&dealership_uid={case['dealerID']}&ordering=vehicle&search=&source=ATC&min_price_change=0&max_price_change=500&page=1&page_size=10", headers={"Authorization": f"Bearer {self.config['manual_token']}"})
                print("Dealer Name: ", case['DealerName'])
                print("Response Status Code: ", response.status_code)
                print("Response: ", response.json() , "\n")
                self.assertEqual(response.status_code, 200)
                self.assertGreater(len(response.json()), 0)

    def test_channel_stat_report_get(self):
        """Test to get response."""
        # Perform a GET request
        for case in self.config['DealerList']:
            with self.subTest(dealerID=case['dealerID']):
                response = requests.get(f"{self.config['BASE_URL']}/api/sales/v2/channel-stats-report?date_from=2024-10-26&date_to=2024-11-01&dealership_uid=6b242ed9-9347-32fb-8d99-2f7fea38d10e&page=1&page_size=10&ordering=&search=&source=GA&inventory=used", headers={"Authorization": f"Bearer {self.config['manual_token']}"})
                print("Dealer Name: ", case['DealerName'])
                print("Response Status Code: ", response.status_code)
                print("Response: ", response.json() , "\n")
                self.assertEqual(response.status_code, 200)
                self.assertGreater(len(response.json()), 0)

    def test_pre_shoot_report_get(self):
        """Test to get response."""
        # Perform a GET request
        for case in self.config['DealerList']:
            with self.subTest(dealerID=case['dealerID']):
                response = requests.get(f"{self.config['BASE_URL']}/api/sales/v2/pre-shoot-report?date_from=2024-10-26&date_to=2024-11-01&dealership_uid=6b242ed9-9347-32fb-8d99-2f7fea38d10e&page=1&page_size=10&ordering=&search=&inventory=used", headers={"Authorization": f"Bearer {self.config['manual_token']}"})
                print("Dealer Name: ", case['DealerName'])
                print("Response Status Code: ", response.status_code)
                print("Response: ", response.json() , "\n")
                self.assertEqual(response.status_code, 200)
                self.assertGreater(len(response.json()), 0)