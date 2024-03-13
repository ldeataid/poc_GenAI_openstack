import json
import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Groups:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch groups")
        response = self.sdk_conn.identity.groups()
        return json.dumps(list(response))

    
    def show(self, group_id):
        if not group_id:
            raise AttributeError("Required attribute 'group_id' was not defined")

        LOG.debug(f"Trying to find '{group_id}' group")
        response = self.sdk_conn.identity.find_group(group_id)
        return json.dumps(response)


    def list_users_in_group(self, group_id):
        if not group_id:
            raise AttributeError("Required attribute 'group_id' was not defined")

        LOG.debug(f"Trying to find users in '{group_id}' group")
        response = self.sdk_conn.identity.group_users(group_id)
        return json.dumps(list(response))


    def check_user_in_group(self, group_id, user_id):
        if not group_id:
            raise AttributeError("Required attribute 'group_id' was not defined")

        if not user_id:
            raise AttributeError("Required attribute 'user_id' was not defined")

        LOG.debug(f"Trying to find user '{user_id}' in '{group_id}' group")
        response = self.sdk_conn.identity.check_user_in_group(user_id, group_id)
        return json.dumps(response)
