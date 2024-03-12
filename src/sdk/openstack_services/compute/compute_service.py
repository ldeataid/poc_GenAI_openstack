from openstack.connection import Connection
from ._servers import Servers


class ComputeService:
    """The compute service (Nova)"""
    
    def __init__(self, conn: Connection):
        sdk_conn = conn
        self.servers = Servers(sdk_conn)
