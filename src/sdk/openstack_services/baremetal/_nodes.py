import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Nodes:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch nodes")
        return self.sdk_conn.baremetal.nodes()

    
    def show(self, node_id):
        if not node_id:
            raise AttributeError("Required attribute 'node_id' was not defined")

        LOG.debug(f"Trying to find '{node_id}' node")
        return self.sdk_conn.baremetal.find_node(node_id)
