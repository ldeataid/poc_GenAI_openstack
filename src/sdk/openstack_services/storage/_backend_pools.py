import json
import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class BackendPools:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch storage backend pools")
        response = self.sdk_conn.block_storage.backend_pools()
        return json.dumps(list(response))
