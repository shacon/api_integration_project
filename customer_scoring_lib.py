import requests
import json

class CustomerScoringClient():

    def __init__(self, base_url="http://not_real.com/customer_scoring?"):
        self.base_url = base_url

    def make_request(self, income, zipcode, age):
        """
        Retrieves the request object with the customer propensity and ranking
        """
        url = self.build_api_url(income, zipcode, age)
        response = requests.get(url)
        status = response.status_code
        if response.ok:
            return response
        elif status == 404:
            raise Exception("Resource not found")
        elif status == 422:
            raise Exception("Invalid input")
        else:
            raise Exception("Error: Status code of" + str(status) + "returned.")

    def build_api_url(self, income, zipcode, age):
        """
        Creates the url string for the api call
        """
        if not self.zipcode_five_digits(zipcode):
            raise Exception("Zip code is improper length")
        params = "income=" + str(income) + "&zipcode=" + str(zipcode) + "&age=" + str(age)
        url = self.base_url + params
        return url

    def zipcode_five_digits(self, zip_code):
        """
        Checks that the given string is five digits
        """
        return len(str(zip_code)) == 5

    def ranking(self, request):
        return request['ranking']

    def propensity(self, request):
        return request['propensity']



