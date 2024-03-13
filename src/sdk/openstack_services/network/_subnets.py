import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Subnets:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch subnets")
        return self.sdk_conn.network.subnets()

    
    def show(self, subnet_id):
        if not subnet_id:
            raise AttributeError("Required attribute 'subnet_id' was not defined")

        LOG.debug(f"Trying to find '{subnet_id}' subnet")
        return self.sdk_conn.network.find_subnet(subnet_id)
