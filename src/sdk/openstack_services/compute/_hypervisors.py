import json
import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Hypervisors:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug(f"Trying to fetch hypervisors")
        response = self.sdk_conn.compute.hypervisors()
        return json.dumps(list(response))


    def show(self, hypervisor_id):
        if not hypervisor_id:
            raise AttributeError("Required attribute 'hypervisor_id' was not defined")

        LOG.debug(f"Trying to find hypervisor '{hypervisor_id}'")
        response = self.sdk_conn.compute.find_hypervisor(hypervisor_id)
        return json.dumps(response)


    def show_uptime(self, hypervisor_id):
        if not hypervisor_id:
            raise AttributeError("Required attribute 'hypervisor_id' was not defined")

        LOG.debug(f"Trying to find hypervisor '{hypervisor_id}' uptime")
        response = self.sdk_conn.compute.get_hypervisor_uptime(hypervisor_id)
        return json.dumps(response)
