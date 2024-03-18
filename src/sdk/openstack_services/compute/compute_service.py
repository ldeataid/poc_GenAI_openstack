from openstack.connection import Connection

from ._availability_zones import AvailabilityZones
from ._flavors import Flavors
from ._hypervisors import Hypervisors
from ._interfaces import ServerInterfaces
from ._keypairs import Keypairs
from ._security_groups import ServerSecurityGroups
from ._server_groups import ServerGroups
from ._servers import Servers
from ._services import Services
from ._volume_attachments import ServerVolumeAttachments


class ComputeService:
    """The compute service (Nova)"""

    def __init__(self, conn: Connection):
        self.availability_zones = AvailabilityZones(conn)
        self.flavors = Flavors(conn)
        self.hypervisors = Hypervisors(conn)
        self.interfaces = ServerInterfaces(conn)
        self.keypairs = Keypairs(conn)
        self.security_groups = ServerSecurityGroups(conn)
        self.server_groups = ServerGroups(conn)
        self.servers = Servers(conn)
        self.services = Services(conn)
        self.volume_attachments = ServerVolumeAttachments(conn)

