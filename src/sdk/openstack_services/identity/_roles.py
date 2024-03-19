import json
import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Roles:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch roles")
        response = self.sdk_conn.identity.roles()
        return json.dumps(list(response))


    def show(self, role_id):
        if not role_id:
            raise AttributeError("Required attribute 'role_id' was not defined")

        LOG.debug(f"Trying to find '{role_id}' role")
        response = self.sdk_conn.identity.find_role(role_id)
        if response is None:
            raise Exception("Role not found!")

        return json.dumps(response)
