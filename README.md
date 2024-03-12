> **_NOTE_**: Many changes were made to have this application run in a container,
> it does not support local runs without changes.

# Openstack ChatBot demo

The purpose of this demo is to demonstrate a chatbot that is capable of make
API requests to the Openstack system, in order to provide the informations to
the user about the Openstack services and cluster, the chatbot uses the OpenAI
LLM and LangChain framework.

## Usage and How-to's

### Requirements

Before starting the execution of the chatbot some steps needs to be done in
order to the chatbot function in its full intention.

First you will need to install the required python libraries, we recommend the
creation of a virtual enviromment.

```shell
git clone https://github.com/Danmcaires/poc_GenAI.git
cd poc_GenAI
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
mkdir certs
```

### Access your Openstack cluster locallyy

After installing the required libraries, start your Openstack cluster. For that,
you can use the [Docs repo](https://github.com/ldeataid/openstack-copilot) as a guide.
If the repo does not appear to you, ask permission from Lucas de Ataides to see it.

If you created your VM according to the docs repo as mentioned above, you don't
need to do the steps bellow, otherwise, here's how you can access the Openstack
APIs locally.

You will need to create a port-forward so the chatbot can access Keystone API of your
cluster. If you are using VirtualBox, to create the port-forward use this command:

```shell
VBoxManage natnetwork modify --netname "NAT_NAME" --port-forward-4 keystone:tcp:[]:<port>:GUEST_IP:<keystone-api-port>"
```

Note that this command assumes that your virtual machine is using a NatNetwork.
Make sure to change `ǸAT_NAME` for the name of you NatNetwork and `GUEST_IP`
for your Keystone API IP.

### ChatGPT API Key

Finally, you will need a valid OpenAI API Key in order to run the chatbot. To
get one visit the [OpenAI website](https://platform.openai.com/docs/overview).
Since OpenAI API is not free, you may need to pay before using the API key.

## Running the chatbot

Now that you made all the necessary configuration, to execute the chatbot run:

```shell
cd $HOME/poc_GenAI; \
source venv/bin/activate; \
source <openstack-openrc-file>; \
python3 src/main.py
```
