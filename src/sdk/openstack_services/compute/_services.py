import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Services:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn

    
    def list(self):
        LOG.debug("Trying to fetch compute services")
        return self.sdk_conn.compute.services()

    
    def show(self, service_id):
        if not service_id:
            raise AttributeError("Required attribute 'service_id' was not defined")

        LOG.debug(f"Trying to find '{service_id}' service")
        return self.sdk_conn.compute.find_service(service_id)
