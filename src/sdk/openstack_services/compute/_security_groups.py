import json
import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class ServerSecurityGroups:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self, server_id):
        if not server_id:
            raise AttributeError("Required attribute 'server_id' was not defined")

        LOG.debug(f"Trying to fetch server '{server_id}' security groups")
        response = self.sdk_conn.compute.fetch_server_security_groups(server_id)
        return json.dumps(list(response))
