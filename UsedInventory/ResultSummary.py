import json
import unittest
import requests
from datetime import datetime

class ResultSummary(unittest.TestCase):
    # Get the current date
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d")  # format as YYYY-MM-DD
    @classmethod
    def setUpClass(cls):
        with open('config.json') as config_file:
            cls.config = json.load(config_file)

    def test_vdps_get(self):
        # Perform a GET request for Total Vdps
        for case in self.config['DealerList']:
            with self.subTest(dealerID=case['dealerID']):
                response = requests.get(f"{self.config['BASE_URL']}/api/sales/v2/result-summary/vdps?dealership_uid={case['dealerID']}&date_to=2024-11-01&last_n_days=30&inventory=used", headers={"Authorization": f"Bearer {self.config['manual_token']}"})
                print("Dealer Name: ", case['DealerName'])
                print("Response Status Code: ", response.status_code)
                print("Response: ", response.json(), "\n")
                self.assertEqual(response.status_code, 200)
                self.assertGreater(len(response.json()), 0)  # Ensure that the response has posts

    def test_sales_get(self):
        # Perform a GET request
        for case in self.config['DealerList']:
            with self.subTest(dealerID=case['dealerID']):
                response = requests.get(f"{self.config['BASE_URL']}/api/sales/v2/result-summary/sales?dealership_uid={case['dealerID']}&date_from=2024-11-01&date_to={self.formatted_date}&inventory=used",headers={"Authorization": f"Bearer {self.config['manual_token']}"})
                print("Dealer Name: ", case['DealerName'])
                print("Response Status Code: ", response.status_code)
                print("Response: ", response.json(), "\n")
                self.assertEqual(response.status_code, 200)
                self.assertGreater(len(response.json()), 0)  # Ensure that the response has posts

    def test_sales_to_flr_get(self):
        # Perform a GET request
        for case in self.config['DealerList']:
            with self.subTest(dealerID=case['dealerID']):
                response = requests.get(f"{self.config['BASE_URL']}/api/sales/v2/sales-to-flr?date_from=2021-01-01&date_to={self.formatted_date}&dealership_uid={case['dealerID']}&inventory=used",headers={"Authorization": f"Bearer {self.config['manual_token']}"})
                print("Dealer Name: ", case['DealerName'])
                print("Response Status Code: ", response.status_code)
                print("Response: ", response.json(), "\n")
                self.assertEqual(response.status_code, 200)
                self.assertGreater(len(response.json()), 0)  # Ensure that the response has posts

    def test_third_party_provider_get(self):
        # Perform a GET request
        for case in self.config['DealerList']:
            with self.subTest(dealerID=case['dealerID']):
                response = requests.get(f"{self.config['BASE_URL']}/api/providers/v2/third-party-provider?dealership_uid={case['dealerID']}&inventory=used",headers={"Authorization": f"Bearer {self.config['manual_token']}"})
                print("Dealer Name: ", case['DealerName'])
                print("Response Status Code: ", response.status_code)
                print("Response: ", response.json(), "\n")
                self.assertEqual(response.status_code, 200)
                self.assertGreater(len(response.json()), 0)  # Ensure that the response has posts

    def test_vdps_by_vehicle_get(self):
        # Perform a GET request
        for case in self.config['DealerList']:
            with self.subTest(dealerID=case['dealerID']):
                response = requests.get(f"{self.config['BASE_URL']}/api/v2/sales/vdps-by-vehicle?dealership_uid={case['dealerID']}&limit=5&inventory=used",headers={"Authorization": f"Bearer {self.config['manual_token']}"})
                print("Dealer Name: ", case['DealerName'])
                print("Response Status Code: ", response.status_code)
                print("Response: ", response.json(), "\n")
                self.assertEqual(response.status_code, 200)
                self.assertGreater(len(response.json()), 0)  # Ensure that the response has posts

    def test_vdps_by_bodystyle_get(self):
        # Perform a GET request
        for case in self.config['DealerList']:
            with self.subTest(dealerID=case['dealerID']):
                response = requests.get(f"{self.config['BASE_URL']}/api/v2/sales/vdps-by-bodystyle?dealership_uid={case['dealerID']}&limit=10&inventory=used",headers={"Authorization": f"Bearer {self.config['manual_token']}"})
                print("Dealer Name: ", case['DealerName'])
                print("Response Status Code: ", response.status_code)
                print("Response: ", response.json(), "\n")
                self.assertEqual(response.status_code, 200)
                self.assertGreater(len(response.json()), 0)  # Ensure that the response has posts

    def test_top_vdps_by_model_get(self):
        # Perform a GET request
        for case in self.config['DealerList']:
            with self.subTest(dealerID=case['dealerID']):
                response = requests.get(f"{self.config['BASE_URL']}/api/v2/sales/top-vdps-by-model?dealership_uid={case['dealerID']}&date_from=2021-01-01&date_to={self.formatted_date}&limit=10&inventory=used",headers={"Authorization": f"Bearer {self.config['manual_token']}"})
                print("Dealer Name: ", case['DealerName'])
                print("Response Status Code: ", response.status_code)
                print("Response: ", response.json(), "\n")
                self.assertEqual(response.status_code, 200)
                self.assertGreater(len(response.json()), 0)  # Ensure that the response has posts

    def test_needs_attention(self):
        # Perform a GET request
        for case in self.config['DealerList']:
            with self.subTest(dealerID=case['dealerID']):
                response = requests.get(f"{self.config['BASE_URL']}/api/v2/reports/needs-attention?date_from=2024-11-01&date_to={self.formatted_date}&dealership_uid={case['dealerID']}&inventory=used",headers={"Authorization": f"Bearer {self.config['manual_token']}"})
                print("Dealer Name: ", case['DealerName'])
                print("Response Status Code: ", response.status_code)
                print("Response: ", response.json(), "\n")
                self.assertEqual(response.status_code, 200)
                self.assertGreater(len(response.json()), 0)  # Ensure that the response has posts

if __name__ == "__main__":
    unittest.main()