import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Keypairs:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn

    
    def list(self):
        LOG.debug("Trying to fetch keypairs")
        return self.sdk_conn.compute.keypairs()

    
    def show(self, keypair_id):
        if not keypair_id:
            raise AttributeError("Required attribute 'keypair_id' was not defined")

        LOG.debug(f"Trying to find '{keypair_id}' keypair")
        return self.sdk_conn.compute.find_keypair(keypair_id)
