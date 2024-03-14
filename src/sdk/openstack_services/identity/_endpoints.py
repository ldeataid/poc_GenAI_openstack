import json
import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Endpoints:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch endpoints")
        response = self.sdk_conn.identity.endpoints()
        return json.dumps(list(response))

    
    def show(self, endpoint_id):
        if not endpoint_id:
            raise AttributeError("Required attribute 'endpoint_id' was not defined")

        LOG.debug(f"Trying to find '{endpoint_id}' endpoint")
        response = self.sdk_conn.identity.find_endpoint(endpoint_id)
        return json.dumps(response)
