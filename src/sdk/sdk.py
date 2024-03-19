import os, sys, json
import logging
import openstack
from openstack.connection import Connection

from openstack_services.baremetal.baremetal_service import BaremetalService
from openstack_services.compute.compute_service import ComputeService
from openstack_services.identity.identity_service import IdentityService
from openstack_services.image.image_service import ImageService
from openstack_services.network.network_service import NetworkService
from openstack_services.storage.storage_service import StorageService


LOG = logging.getLogger("openstacksdk")


class OpenstackSdk:
    def __init__(self):
        self.create_logger()
        self.confirm_required_variables_defined()

        # Enable SDK debug
        try:
            if os.environ["SDK_DEBUG"].lower() == "true":
                openstack.enable_logging(debug=True)
        except KeyError:
            LOG.info("Variable SDK_DEBUG is not defined. Skipping SDK logging config")

        # Connect to the Openstack Cloud
        try:
            openstack_cloud_name = os.environ["OS_CLOUD_NAME"] 
            LOG.info(f"Trying to connect to Openstack cloud '{openstack_cloud_name}'")
            sdk_conn = openstack.connect(cloud=openstack_cloud_name)
            LOG.info(f"Successfully connected to Openstack cloud '{openstack_cloud_name}'")
        except Exception as e:
            msg = "Something went wrong when trying to connect to the Openstack cloud: %s", repr(e)
            print(msg)
            LOG.error(msg)
            sys.exit(1)

        # Load all available Openstack services
        self.openstack_services_mixin(sdk_conn)
        self.enabled_services = self.list_active_openstack_services()


    def create_logger(self, loglevel=logging.DEBUG):
        # Create logger
        LOG = logging.getLogger("openstacksdk")
        LOG.setLevel(loglevel)

        # Create a file handler and set its level to INFO
        file_handler = logging.FileHandler('openstacksdk.log')
        file_handler.setLevel(loglevel)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # Add the file handler to the logger
        LOG.addHandler(file_handler)
        LOG.info("OpenstackSDK logger initiated.")


    def confirm_required_variables_defined(self):
        os_variables = ["OS_CLOUD_NAME", "OS_AUTH_URL", "OS_USERNAME",
                        "OS_PASSWORD", "OS_PROJECT_DOMAIN_NAME",
                        "OS_PROJECT_NAME", "OS_USER_DOMAIN_NAME"]
        for os_var in os_variables:
            try:
                os.environ[os_var]
            except KeyError:
                msg = f"Required environment variable {os_var} is not defined. Exiting"
                print(msg)
                LOG.info(msg)
                sys.exit(1)


    def openstack_services_mixin(self, sdk_conn: Connection):
        self.BAREMETAL = BaremetalService(sdk_conn)
        self.NOVA = ComputeService(sdk_conn)
        self.KEYSTONE = IdentityService(sdk_conn)
        self.GLANCE = ImageService(sdk_conn)
        self.NEUTRON = NetworkService(sdk_conn)
        self.CINDERV3 = StorageService(sdk_conn)


    def list_active_openstack_services(self):
        sdk_services_response = self.KEYSTONE.services.list()
        sdk_services = json.loads(sdk_services_response)
        active_services = []
        for service in sdk_services:
            if service["is_enabled"]:
                active_services.append(service["name"])
        return active_services


# Uncomment the lines below if you want to test
# the OpenstackSDK only
# if __name__ == "__main__":
#     sdk = OpenstackSdk()
#     print(sdk.NOVA.servers.list())
#     print(sdk.NOVA.servers.show("vm2"))
#     print(sdk.CINDERV3.volumes.list())
#     print(sdk.CINDERV3.volumes.show("test-volume-1"))
#     print(sdk.CINDERV3.backups.list())
#     print(sdk.KEYSTONE.services.list())
#     print(sdk.KEYSTONE.services.show("cinderv3"))
#     print(sdk.NEUTRON.routers.list())
#     print(sdk.NEUTRON.routers.show("demo-router"))
#     print(sdk.NOVA.hypervisors.list())
#     print(sdk.NOVA.hypervisors.show("openstack"))
#     print(sdk.NOVA.services.list())
#     print(sdk.NEUTRON.agents.list())
#     print(sdk.NOVA.hypervisors.list())
