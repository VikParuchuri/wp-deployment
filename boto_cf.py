import boto.cloudformation
import os

boto.set_stream_logger(__name__)

ROOT_PATH = os.path.abspath(__file__)
CF_PATH = os.path.abspath(os.path.join(ROOT_PATH, "cloudformation"))

REGION = "us-east-1"
TEMPLATE_FILE_NAME = "wordpress.json"

TEMPLATE_FILE_PATH = os.path.abspath(os.path.join(CF_PATH, TEMPLATE_FILE_NAME))

template_data = open(TEMPLATE_FILE_PATH).read()

parameters = [("KeyName", "VikLinux")]

conn = boto.cloudformation.connection.CloudFormationConnection()

def validate_template(template_data):
    conn.validate_template(template_body=template_data)

def create_template(stack_name, template_data, parameters, disable_rollback=False):
    conn.create_stack(stack_name, template_body=template_data, parameters=parameters, notification_arns=[], disable_rollback=disable_rollback)
