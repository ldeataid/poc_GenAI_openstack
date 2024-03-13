from openstack.connection import Connection

from ._credentials import Credentials
from ._domains import Domains
from ._endpoints import Endpoints
from ._groups import Groups
from ._policies import Policies
from ._projects import Projects
from ._regions import Regions
from ._roles import Roles
from ._services import Services
from ._users import Users


class IdentityService:
    """The identity service (Keystone)"""
    
    def __init__(self, conn: Connection):
        self.credentials = Credentials(conn)
        self.domains = Domains(conn)
        self.endpoints = Endpoints(conn)
        self.groups = Groups(conn)
        self.policies = Policies(conn)
        self.projects = Projects(conn)
        self.regions = Regions(conn)
        self.roles = Roles(conn)
        self.services = Services(conn)
        self.users = Users(conn)
