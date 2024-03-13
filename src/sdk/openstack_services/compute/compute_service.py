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
        sdk_conn = conn
        
        self.availability_zones = AvailabilityZones(sdk_conn)
        self.flavors = Flavors(sdk_conn)
        self.hypervisors = Hypervisors(sdk_conn)
        self.interfaces = ServerInterfaces(sdk_conn)
        self.keypairs = Keypairs(sdk_conn)
        self.security_groups = ServerSecurityGroups(sdk_conn)
        self.server_groups = ServerGroups(sdk_conn)
        self.servers = Servers(sdk_conn)
        self.services = Services(sdk_conn)
        self.volume_attachments = ServerVolumeAttachments(sdk_conn)

