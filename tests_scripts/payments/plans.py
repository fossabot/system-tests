from .base_stripe import BaseStripe
from time import sleep


class Plans(BaseStripe):
    '''
        check that the plans are configured correctly on backend, and have the expected prices on process.
        result is compared to 'self.expected_prices'
    '''
    def __init__(self, test_obj=None, backend=None, kubernetes_obj=None, test_driver=None):
        super(Plans, self).__init__(test_obj=test_obj, backend=backend, test_driver=test_driver)
    
    def start(self):
        response = self.backend.get_stripe_plans()
        assert response.status_code == 200, f"expected status code 200, found {response.status_code}. Make sure you have a valid stripe secret key and priceIdsMap is well configured"

        for plan in response.json():
            name = plan["name"]
            price = plan["price"]
            assert name in [price["name"] for price in self.expected_prices], f"price plan '{name}' not found in response"
            expected_price = [price["price"] for price in self.expected_prices if price["name"] == name][0]
            assert price == expected_price, f"expected price of plan '{name}' = '{expected_price}', found '{price}' "

        return self.cleanup()



