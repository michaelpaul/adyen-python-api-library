from ..base import AdyenServiceBase


class GeneralApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(GeneralApi, self).__init__(client=client)
        self.service = "payments"

    def create_authorisation(self, request, idempotency_key=None, **kwargs):
        """
        Create an authorisation
        """
        endpoint = f"/authorise"
        endpoint = endpoint.replace('/', '', 1)
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def complete3ds_authorisation(self, request, idempotency_key=None, **kwargs):
        """
        Complete a 3DS authorisation
        """
        endpoint = f"/authorise3d"
        endpoint = endpoint.replace('/', '', 1)
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def complete3ds2_authorisation(self, request, idempotency_key=None, **kwargs):
        """
        Complete a 3DS2 authorisation
        """
        endpoint = f"/authorise3ds2"
        endpoint = endpoint.replace('/', '', 1)
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_the3ds_authentication_result(self, request, idempotency_key=None, **kwargs):
        """
        Get the 3DS authentication result
        """
        endpoint = f"/getAuthenticationResult"
        endpoint = endpoint.replace('/', '', 1)
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_the3ds2_authentication_result(self, request, idempotency_key=None, **kwargs):
        """
        Get the 3DS2 authentication result
        """
        endpoint = f"/retrieve3ds2Result"
        endpoint = endpoint.replace('/', '', 1)
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

