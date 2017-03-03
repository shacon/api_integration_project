import unittest
import customer_scoring_lib as cs_lib

class TestApiIntegrationApp(unittest.TestCase):

    def setUp(self):
        self.sample_json = {
            "propensity": 0.26532,
            "ranking": "C"
        }
        self.client = cs_lib.CustomerScoringClient()

    def test_build_api_url(self):
        expected_url = 'http://not_real.com/customer_scoring?income=50000&zipcode=60201&age=35'
        self.assertEqual(self.client.build_api_url(50000, 60201, 35), expected_url)

    def test_ranking(self):
        self.assertEqual(self.client.ranking(self.sample_json), 'C')

    def test_propensity(self):
        self.assertEqual(self.client.propensity(self.sample_json), 0.26532)

    def test_zipcode_five_digits(self):
        self.assertEqual(self.client.zipcode_five_digits(60640), True)

    def test_zipcode_five_digits_returns_false(self):
        self.assertEqual(self.client.zipcode_five_digits(6064048), False)
        self.assertEqual(self.client.zipcode_five_digits(60), False)
        with self.assertRaises(Exception) as cm:
            self.client.build_api_url(40000,383838383,36)
        self.assertEqual(
        'Zip code is improper length',
        str(cm.exception)
)


if __name__ == "__main__":
    unittest.main()




