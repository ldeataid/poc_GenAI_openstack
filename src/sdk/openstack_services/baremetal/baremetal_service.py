from openstack.connection import Connection

from ._nodes import Nodes


class BaremetalService:
    """The baremetal service"""

    def __init__(self, conn: Connection):
        self.nodes = Nodes(conn)
