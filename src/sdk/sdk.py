import os, sys
import logging
import openstack
from openstack_services.identity.identity_service import IdentityService
from openstack_services.compute.compute_service import ComputeService


LOG = logging.getLogger("openstacksdk")


class OpenstackSdk:
    def __init__(self):
        self.create_logger()
        self.confirm_required_variables_defined()
        
        # Enable SDK debug
        try:
            openstack.enable_logging(debug=os.environ["SDK_DEBUG"])
        except KeyError:
            LOG.info("Variable SDK_DEBUG is not defined. Skipping SDK logging config")

        # Connect to the Openstack Cloud
        try:
            openstack_cloud_name = os.environ["OS_CLOUD_NAME"] 
            LOG.info(f"Trying to connect to Openstack cloud '{openstack_cloud_name}'")
            sdk_conn = openstack.connect(cloud=openstack_cloud_name)
            LOG.info(f"Successfully connected to Openstack cloud '{openstack_cloud_name}'")
        except Exception as e:
            LOG.error("Something went wrong when trying to connect to the Openstack cloud: %s", repr(e))

        # Define all services
        self.IDENTITY = IdentityService(sdk_conn)
        self.COMPUTE = ComputeService(sdk_conn)


    def create_logger(self, loglevel=logging.INFO):
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
                LOG.info(f"Required environment variable {os_var} is not defined. Exiting")
                sys.exit(1)


if __name__ == "__main__":
    sdk = OpenstackSdk()
    teste = 'sdk.COMPUTE.servers.show("test-vm")'
    print(eval(teste))
