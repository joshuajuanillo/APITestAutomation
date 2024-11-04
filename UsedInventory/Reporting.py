import json
import unittest
import requests

class Reporting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('config.json') as config_file:
            cls.config = json.load(config_file)

    def test_advance_report_leads_get(self):
        """Test to get response."""
        # Perform a GET request
        for case in self.config['DealerList']:
            with self.subTest(dealerID=case['dealerID']):
                response = requests.get(f"{self.config['BASE_URL']}/api/statistics/v2/advanced-reports?dol_max=2000&dol_min=0&date_from=2021-01-01&date_to=2024-11-01&dealership_uid={case['dealerID']}&page=1&page_size=10&order=-total_leads&ordering=&search=&inventory=used", headers={"Authorization": f"Bearer {self.config['manual_token']}"})
                print("Dealer Name: ", case['DealerName'])
                print("Response Status Code: ", response.status_code)
                print("Response: ", response.json(), "\n")
                self.assertEqual(response.status_code, 200)
                self.assertGreater(len(response.json()), 0)

    def test_advance_report_most_vdps_get(self):
        """Test to get response."""
        # Perform a GET request
        for case in self.config['DealerList']:
            with self.subTest(dealerID=case['dealerID']):
                response = requests.get(f"{self.config['BASE_URL']}/api/statistics/v2/advanced-reports?date_from=2021-01-01&date_to=2024-11-01&dealership_uid={case['dealerID']}&page=1&page_size=10&order=-total_vdps&ordering=&search=&inventory=used", headers={"Authorization": f"Bearer {self.config['manual_token']}"})
                print("Dealer Name: ", case['DealerName'])
                print("Response Status Code: ", response.status_code)
                print("Response: ", response.json(), "\n")
                self.assertEqual(response.status_code, 200)
                self.assertGreater(len(response.json()), 0)

    def test_advance_report_least_vdps_get(self):
        """Test to get response."""
        # Perform a GET request
        for case in self.config['DealerList']:
            with self.subTest(dealerID=case['dealerID']):
                response = requests.get(f"{self.config['BASE_URL']}/api/statistics/v2/advanced-reports?date_from=2021-01-01&date_to=2024-11-01&dealership_uid={case['dealerID']}&page=1&page_size=10&order=total_vdps&ordering=&search=&inventory=used", headers={"Authorization": f"Bearer {self.config['manual_token']}"})
                print("Dealer Name: ", case['DealerName'])
                print("Response Status Code: ", response.status_code)
                print("Response: ", response.json(), "\n")
                self.assertEqual(response.status_code, 200)
                self.assertGreater(len(response.json()), 0)

    def test_advance_report_days_on_lot_get(self):
        """Test to get VDPS response."""
        # Perform a GET request
        for case in self.config['DealerList']:
            with self.subTest(dealerID=case['dealerID']):
                response = requests.get(f"{self.config['BASE_URL']}/api/statistics/v2/advanced-reports?dol_max=2000&dol_min=0&date_from=2021-01-01&date_to=2024-11-01&dealership_uid={case['dealerID']}&page=1&page_size=10&order=-dol&ordering=&search=&inventory=used", headers={"Authorization": f"Bearer {self.config['manual_token']}"})
                print("Dealer Name: ", case['DealerName'])
                print("Response Status Code: ", response.status_code)
                print("Response: ", response.json(), "\n")
                self.assertEqual(response.status_code, 200)
                self.assertGreater(len(response.json()), 0)

    def test_advance_report_vdp_boost_get(self):
        """Test to get VDPS response."""
        # Perform a GET request
        for case in self.config['DealerList']:
            with self.subTest(dealerID=case['dealerID']):
                response = requests.get(f"{self.config['BASE_URL']}/api/boost/vdp-boost?dealership_uid={case['dealerID']}&inventory=used&search=", headers={"Authorization": f"Bearer {self.config['manual_token']}"})
                print("Dealer Name: ", case['DealerName'])
                print("Response Status Code: ", response.status_code)
                print("Response: ", response.json(), "\n")
                self.assertEqual(response.status_code, 200)
                self.assertGreater(len(response.json()), 0)