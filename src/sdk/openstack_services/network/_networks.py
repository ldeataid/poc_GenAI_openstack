import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Networks:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch networks")
        return self.sdk_conn.network.networks()

    
    def show(self, network_id):
        if not network_id:
            raise AttributeError("Required attribute 'network_id' was not defined")

        LOG.debug(f"Trying to find '{network_id}' network")
        return self.sdk_conn.network.find_network(network_id)
