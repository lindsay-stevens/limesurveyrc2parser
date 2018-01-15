from urllib.request import urlopen, Request
from urllib.parse import urlencode
import json
from collections import OrderedDict


class LimeSurveyError(Exception):
    """Base class for exceptions in LimeSurvey."""
    def __init__(self, method, *args):
        base_err = "Error during query"
        message = [base_err, method]
        if args is not None:
            message += [str(x) for x in args]
        self.message = " | ".join(message)


class LimeSurveyClient(object):

    def __init__(self, url):
        self.headers = {"content-type": "application/json"}
        self.url = url

    def query(self, method, params):
        """
        Query the LimeSurvey API

        Important! Despite being provided as key-value, the API treats all
        parameters as positional. OrderedDict should be used to ensure this,
        otherwise some calls may randomly fail.

        Parameters
        :param method: Name of API method to call.
        :type method: String
        :param params: Parameters to the specified API call.
        :type params: OrderedDict

        Return
        :return: result of API call
        :raise: requests.ConnectionError
        :raise: LimeSurveyError if the API returns an error (either http error
            or error message in body)
        """
        # 1. Prepare the request data
        data = OrderedDict([
            ("method", method),
            ("params", params),
            ("id", 1)  # Possibly a request id for parallel use cases.
        ])

        # 2. Query the API
        param_data = urlencode(data).encode("ascii")
        req = Request(url=self.url, data=param_data, headers=self.headers)
        with urlopen(req, data=param_data) as response:
            content = response.read().decode("utf-8")

        if response.status != 200:
            raise LimeSurveyError(
                method, "Not response.ok", response.status,
                content)

        if not 0 < len(content):
            raise LimeSurveyError(
                method, "Not 0 < len(response.content)",
                response.status, content)

        response_data = json.loads(content)

        try:
            return_value = response_data.get("result")
        except KeyError:
            raise LimeSurveyError(
                method, "Key 'result' not in response json",
                response.status, content)

        return return_value
#METHODSPLACEHOLDER