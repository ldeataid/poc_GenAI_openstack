import json
import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Credentials:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch credentials")
        response = self.sdk_conn.identity.credentials()
        return json.dumps(list(response))

    
    def show(self, credential_id):
        if not credential_id:
            raise AttributeError("Required attribute 'credential_id' was not defined")

        LOG.debug(f"Trying to find '{credential_id}' credential")
        response = self.sdk_conn.identity.find_credential(credential_id)
        return json.dumps(response)
