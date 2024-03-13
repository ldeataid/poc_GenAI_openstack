import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Roles:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch roles")
        return self.sdk_conn.identity.roles()

    
    def show(self, role_id):
        if not role_id:
            raise AttributeError("Required attribute 'role_id' was not defined")

        LOG.debug(f"Trying to find '{role_id}' role")
        return self.sdk_conn.identity.find_role(role_id)
