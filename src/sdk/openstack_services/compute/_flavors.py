import json
import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Flavors:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch flavors")
        response = self.sdk_conn.compute.flavors()
        return json.dumps(list(response))


    def show(self, flavor_id):
        if not flavor_id:
            raise AttributeError("Required attribute 'flavor_id' was not defined")

        LOG.debug(f"Trying to find '{flavor_id}' flavor")
        response = self.sdk_conn.compute.find_flavor(flavor_id)
        if response is None:
            raise Exception("Flavor not found!")
        return json.dumps(response)


    def show_extra_specs(self, flavor_id):
        if not flavor_id:
            raise AttributeError("Required attribute 'flavor_id' was not defined")

        LOG.debug(f"Trying to find '{flavor_id}' flavor's extra specs")
        response = self.sdk_conn.compute.fetch_flavor_extra_specs(flavor_id)
        if response is None:
            raise Exception("Flavor not found!")
        return json.dumps(list(response))


    def show_access(self, flavor_id):
        if not flavor_id:
            raise AttributeError("Required attribute 'flavor_id' was not defined")

        LOG.debug(f"Trying to find users who have access to flavor '{flavor_id}'")
        response = self.sdk_conn.compute.get_flavor_access(flavor_id)
        if response is None:
            raise Exception("Flavor not found!")

        return json.dumps(list(response))
