import json
import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Nodes:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch nodes")
        response = self.sdk_conn.baremetal.nodes()
        return json.dumps(list(response))


    def show(self, node_id):
        if not node_id:
            raise AttributeError("Required attribute 'node_id' was not defined")

        LOG.debug(f"Trying to find '{node_id}' node")
        response = self.sdk_conn.baremetal.find_node(node_id)
        return json.dumps(response)
