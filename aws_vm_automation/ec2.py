import boto3

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
