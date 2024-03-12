import os, sys
import logging
import openstack


LOG = logging.getLogger("openstacksdk")


class OpenstackSdk:
    def __init__(self):
        self.create_logger()
        self.confirm_required_variables_defined()
        
        try:
            openstack.enable_logging(debug=os.environ["SDK_DEBUG"])
        except KeyError:
            LOG.info("Variable SDK_DEBUG is not defined. Skipping SDK logging config")
        
        try:
            openstack_cloud_name = os.environ["OS_CLOUD_NAME"] 
            LOG.info(f"Trying to connect to Openstack cloud '{openstack_cloud_name}'")
            self.sdk_conn = openstack.connect(cloud=openstack_cloud_name)
            LOG.info(f"Successfully connected to Openstack cloud '{openstack_cloud_name}'")
        except Exception as e:
            LOG.error("Something went wrong when trying to connect to the Openstack cloud: %s", repr(e))


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


    def test(self):
        for service in self.sdk_conn.identity.services():
            print(service)


if __name__ == "__main__":
    sdk = OpenstackSdk()
    sdk.test()
