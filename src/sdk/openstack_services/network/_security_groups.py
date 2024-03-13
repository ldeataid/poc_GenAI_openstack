import json
import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class SecurityGroups:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch security groups")
        response = self.sdk_conn.network.security_groups()
        return json.dumps(list(response))

    
    def show(self, security_group_id):
        if not security_group_id:
            raise AttributeError("Required attribute 'security_group_id' was not defined")

        LOG.debug(f"Trying to find '{security_group_id}' security group")
        response = self.sdk_conn.network.find_security_group(security_group_id)
        return json.dumps(response)
