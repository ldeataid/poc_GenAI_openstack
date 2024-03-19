import json
import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Services:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch block storage services")
        response = self.sdk_conn.block_storage.services()
        return json.dumps(list(response))


    def show(self, service_id):
        if not service_id:
            raise AttributeError("Required attribute 'service_id' was not defined")

        LOG.debug(f"Trying to find '{service_id}' service")
        response = self.sdk_conn.block_storage.find_service(service_id)
        if response is None:
            raise Exception("Service not found!")

        return json.dumps(response)
