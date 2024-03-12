import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Servers:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn

    
    def list(self):
        LOG.debug("Trying to fetch servers")
        return self.sdk_conn.compute.servers()

    
    def show(self, server_id):
        if not server_id:
            raise AttributeError("Required attribute 'server_id' was not defined")

        LOG.debug(f"Trying to find '{server_id}' server")
        return self.sdk_conn.compute.find_server(server_id)


    def show_metadata(self, server_id):
        if not server_id:
            raise AttributeError("Required attribute 'server_id' was not defined")

        LOG.debug(f"Trying to find '{server_id}' server")
        return self.sdk_conn.compute.get_server_metadata(server_id)
