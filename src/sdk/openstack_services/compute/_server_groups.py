import json
import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class ServerGroups:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch server_groups")
        all_projects = True if self.sdk_conn.auth["username"] == "admin" else False
        response = self.sdk_conn.compute.server_groups(all_projects=all_projects)
        return json.dumps(list(response))


    def show(self, server_group_id):
        if not server_group_id:
            raise AttributeError("Required attribute 'server_group_id' was not defined")

        LOG.debug(f"Trying to find '{server_group_id}' server group")
        all_projects = True if self.sdk_conn.auth["username"] == "admin" else False
        response = self.sdk_conn.compute.find_server_group(server_group_id, all_projects=all_projects)
        if response is None:
            raise Exception("Server group not found!")

        return json.dumps(response)
