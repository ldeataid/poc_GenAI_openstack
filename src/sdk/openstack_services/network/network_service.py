from openstack.connection import Connection

from ._agents import Agents
from ._networks import Networks
from ._pools import Pools
from ._ports import Ports
from ._routers import Routers
from ._security_groups import SecurityGroups
from ._subnets import Subnets


class NetworkService:
    """The network service (Neutron)"""
    
    def __init__(self, conn: Connection):
        sdk_conn = conn

        self.agents = Agents(sdk_conn)
        self.networks = Networks(sdk_conn)
        self.pools = Pools(sdk_conn)
        self.ports = Ports(sdk_conn)
        self.routers = Routers(sdk_conn)
        self.security_groups = SecurityGroups(sdk_conn)
        self.subnets = Subnets(sdk_conn)
