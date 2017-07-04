import json
import pytest


class TestSubscriptionField(object):
    def test_subscription_field1(self, tmp_app2):
        """ GIVEN
        """
        """ tmp_app2 """

        """ WHEN
        """
        resp = tmp_app2.post("/very/scary/hello/machine/")
        resp_dict = json.loads(resp.data.decode())

        """ THEN
        """
        assert "At the time when I had 99 tacos." == resp_dict["input_date"]
        assert "SungPilPaek" == resp_dict["username"]
        with pytest.raises(KeyError):
            assert "Nice to meet you!!" == resp_dict["Hello!!"]