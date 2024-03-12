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
        sdk_conn = conn
        self.credentials = Credentials(sdk_conn)
        self.domains = Domains(sdk_conn)
        self.endpoints = Endpoints(sdk_conn)
        self.groups = Groups(sdk_conn)
        self.policies = Policies(sdk_conn)
        self.projects = Projects(sdk_conn)
        self.regions = Regions(sdk_conn)
        self.roles = Roles(sdk_conn)
        self.services = Services(sdk_conn)
        self.users = Users(sdk_conn)
