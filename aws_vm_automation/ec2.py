from typing import Optional
import boto3

UBUNTU_OWNER_CANONICAL = "099720109477"
UBUNTU_2204_NAME_PATTERN = "ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"

def find_latest_ubuntu_ami(region: str) -> str:
    ec2 = boto3.client("ec2", region_name=region)

    response = ec2.describe_images(
        Owners=["099720109477"],  # Canonical (Ubuntu official)
        Filters=[
            {
                "Name": "name",
                "Values": ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"],
            },
            {
                "Name": "architecture",
                "Values": ["x86_64"],
            },
        ],
    )

    images = response["Images"]
    images.sort(key=lambda img: img["CreationDate"])

    latest_image = images[-1]
    return latest_image["ImageId"]


def create_instance(
    region: str,
    key_name: str,
    instance_type: str = "t2.micro",
) -> str:
    ec2 = boto3.client("ec2", region_name=region)
    ami_id = find_latest_ubuntu_ami(region)

    resp = ec2.run_instances(
        ImageId=ami_id,
        InstanceType=instance_type,
        KeyName=key_name,
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[
            {
                "ResourceType": "instance",
                "Tags": [
                    {"Key": "Project", "Value": "aws-vm-automation"},
                ],
            }
        ],
    )

    instance_id = resp["Instances"][0]["InstanceId"]
    return instance_id


def wait_until_running(region: str, instance_id: str) -> None:
    ec2 = boto3.client("ec2", region_name=region)
    waiter = ec2.get_waiter("instance_running")
    waiter.wait(InstanceIds=[instance_id])


def get_public_ip(region: str, instance_id: str) -> Optional[str]:
    ec2 = boto3.client("ec2", region_name=region)
    resp = ec2.describe_instances(InstanceIds=[instance_id])
    inst = resp["Reservations"][0]["Instances"][0]
    return inst.get("PublicIpAddress")


def terminate_instance(region: str, instance_id: str) -> None:
    ec2 = boto3.client("ec2", region_name=region)
    ec2.terminate_instances(InstanceIds=[instance_id])
    waiter = ec2.get_waiter("instance_terminated")
    waiter.wait(InstanceIds=[instance_id])