import json
import pytest


class TestSubscriptionParser(object):
    def test_subscription_parser1(self, tmp_test_client2):
        """ GIVEN
        """
        """ tmp_test_client2 """

        """ WHEN
        """
        resp = tmp_test_client2.get("/very/scary/hello/machine/?index=228&abc=def")
        resp_dict = json.loads(resp.data.decode())

        """ THEN
        """
        assert "200 OK" == resp.status
        assert "228" == resp_dict["index"]
        with pytest.raises(KeyError):
            assert 1 == resp_dict["abc"]