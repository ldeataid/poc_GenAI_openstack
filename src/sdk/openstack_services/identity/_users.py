import json
import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Users:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch users")
        response = self.sdk_conn.identity.users()
        return json.dumps(list(response))

    
    def show(self, user_id):
        if not user_id:
            raise AttributeError("Required attribute 'user_id' was not defined")

        LOG.debug(f"Trying to find '{user_id}' user")
        response = self.sdk_conn.identity.find_user(user_id)
        return json.dumps(response)
