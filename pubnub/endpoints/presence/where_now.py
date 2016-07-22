import six

from pubnub.endpoints.endpoint import Endpoint
from pubnub.enums import HttpMethod, PNOperationType
from pubnub.errors import PNERR_UUID_MISSING
from pubnub.exceptions import PubNubException


class WhereNow(Endpoint):
    # /v2/presence/sub-key/<subscribe_key>/uuid/<uuid>
    WHERE_NOW_PATH = "/v2/presence/sub-key/%s/uuid/%s"

    def __init__(self, pubnub):
        Endpoint.__init__(self, pubnub)
        self._uuid = None

    def uuid(self, uuid):
        self._uuid = uuid
        return self

    def build_params(self):
        return self.default_params()

    def build_path(self):
        return WhereNow.WHERE_NOW_PATH % (self.pubnub.config.subscribe_key, self._uuid)

    def http_method(self):
        return HttpMethod.GET

    def validate_params(self):
        self.validate_subscribe_key()

        if self._uuid is None or not isinstance(self._uuid, six.string_types):
            raise PubNubException(pn_error=PNERR_UUID_MISSING)

    def create_response(self, envelope):
        pass
        # return PNHereNowResult.from_json(envelope, self._channels)

    def request_timeout(self):
        return self.pubnub.config.non_subscribe_request_timeout

    def connect_timeout(self):
        return self.pubnub.config.connect_timeout

    def operation_type(self):
        return PNOperationType.PNWhereNowOperation

    def name(self):
        return "WhereNow"
