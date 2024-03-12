from openstack.connection import Connection
from ._services import Services


class IdentityService:
    """The identity service (Keystone)"""
    
    def __init__(self, conn: Connection):
        sdk_conn = conn
        self.services = Services(sdk_conn)
