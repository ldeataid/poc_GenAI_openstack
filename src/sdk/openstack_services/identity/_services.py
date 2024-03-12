import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Services:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn

    
    def list(self):
        LOG.debug("Trying to fetch services")
        return self.sdk_conn.identity.services()

    
    def show(self, service_name):
        if not service_name:
            raise AttributeError("Required attribute 'service_name' was not defined")

        LOG.debug(f"Trying to find '{service_name}' service")
        return self.sdk_conn.identity.find_service(service_name)
