import json
import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Policies:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch policies")
        response = self.sdk_conn.identity.policies()
        return json.dumps(list(response))


    def show(self, policy_id):
        if not policy_id:
            raise AttributeError("Required attribute 'policy_id' was not defined")

        LOG.debug(f"Trying to find '{policy_id}' policy")
        response = self.sdk_conn.identity.find_policy(policy_id)
        if response is None:
            raise Exception("Policy not found!")

        return json.dumps(response)
