import json
import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Services:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch all services")
        response = self.sdk_conn.identity.services()
        return json.dumps(list(response))

    
    def show(self, service_id):
        if not service_id:
            raise AttributeError("Required attribute 'service_id' was not defined")

        LOG.debug(f"Trying to find '{service_id}' service")
        response = self.sdk_conn.identity.find_service(service_id)
        return json.dumps(response)