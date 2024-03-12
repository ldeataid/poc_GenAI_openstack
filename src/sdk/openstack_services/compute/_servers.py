import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Servers:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn

    
    def list(self):
        LOG.debug("Trying to fetch servers")
        return self.sdk_conn.compute.servers()

    
    def show(self, server_name):
        if not server_name:
            raise AttributeError("Required attribute 'server_name' was not defined")

        LOG.debug(f"Trying to find '{server_name}' server")
        return self.sdk_conn.compute.find_server(server_name)
