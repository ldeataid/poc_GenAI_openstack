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
        self.agents = Agents(conn)
        self.networks = Networks(conn)
        self.pools = Pools(conn)
        self.ports = Ports(conn)
        self.routers = Routers(conn)
        self.security_groups = SecurityGroups(conn)
        self.subnets = Subnets(conn)
