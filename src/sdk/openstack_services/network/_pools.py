import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Pools:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch pools")
        return self.sdk_conn.network.pools()

    
    def show(self, pool_id):
        if not pool_id:
            raise AttributeError("Required attribute 'pool_id' was not defined")

        LOG.debug(f"Trying to find '{pool_id}' pool")
        return self.sdk_conn.network.find_pool(pool_id)
