import sys
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from constants import LOG
import requests
import re
import os

class openstack_request():

    def __init__(self, user_query, key):
        # Load env variables
        self.auth_url = os.environ['OS_IP']
        self.user = os.environ['OS_USER']
        self.password = os.environ['OS_PASSWORD']
        self.domain_name = os.environ['OS_DOMAIN_NAME']

        # Necessary API address
        pattern = r"(https?)://(?:\d{1,3}\.){3}\d{1,3}:"
        match = re.search(pattern, self.auth_url)
        self.api_server_url = match.group(0)

        # Necessary token
        self.token = self.get_token()

        # API key
        self.api_key = key

        # User query
        self.query = user_query

        # Embedded list of Wind River APIs
        self.apis = self.load_embedded_apis()


    def load_embedded_apis(self):
        with open ("openstack_apis.json", "r") as f:
            api_list = f.read()

        return api_list


    def get_endpoint(self):
        completion = self.get_api_completion()
        api = self.api_server_url + completion

        return api


    def get_api_completion(self):
        # Initiate OpenAI
        llm = ChatOpenAI(openai_api_key = self.api_key,
                         temperature=0.4)

        # Expected llm response format
        format_response = "api: <api_url>"

        # Create prompt
        prompt = ChatPromptTemplate.from_messages([
        ("system", f"You are an API generator, based on the user question you will suggest the best API endpoint to retrieve the information from a OpenStack platform.\n\nYou will look in the context for the available APIs in OpenStack platform.\n\nMake sure the provided endpoint is present on the provided context and check the action of the APIs to provide the ideal url for the user question.\n\nAlso make sure to only provide the API endpoint following the format: {format_response}. Guarantee that the format is followed. Read the entire context before providing an answer."),
        ("user", "Context:{context} \n\n\n Question:{question}")
        ])

        output_parser = StrOutputParser()
        chain = prompt | llm | output_parser

        #Get completion
        completion = chain.invoke({"context":self.apis, "question": self.query})

        #completion = response.choices[0].message.content
        clean_completion = completion.split(":")[1].strip()

        return clean_completion


    def get_API_response(self):
        url = self.get_endpoint()
        headers = {
            "X-Auth-Token": self.token
        }


        try:
            print(f'API address: {url}', file=sys.stderr)
            LOG.info(f'API address: {url}')
            response = requests.get(url, headers=headers, verify=False)
        except Exception as e:
            error = f"An error ocurred while trying to retrieve the information, please rewrite the question and try again.\n Error: {e}"
            LOG.warning(error)
            return error

        if response.status_code == 200:
            str_response = f"OpenStack API response = {response.text}"
            return str_response
        else:
            error = f"Error trying to make API request:\n {response.status_code}, {response.text}"
            LOG.warning(error)
            return error



    def get_token(self):
        url = f"{self.auth_url}/v{self.auth_version}/auth/tokens?nocatalog"
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "auth": {
                "identity": {
                    "methods": ["password"],
                    "password": {
                        "user": {
                            "name": self.user,
                            "domain": {"name": self.domain_name},
                            "password": self.password
                        }
                    }
                },
                "scope": {
                    "project": {
                        "name": self.user,
                        "domain": {"name": self.domain_name}
                    }
                }
            }
        }

        try:
            response = requests.post(url, headers=headers, json=data, verify=False)
        except Exception as e:
            error = f"An error ocurred while trying to retrieve the authentication for the OpenStack APIs. Error:{e}"
            LOG.error(error)
            return error

        if response.status_code == 201:
            # Get token from response
            x_auth_token = response.headers.get("X-Subject-Token")

            return x_auth_token
        else:
            error = f"Error trying to retrieve authentication token:\n {response.status_code}, {response.text}"
            LOG.warning(error)
            return error