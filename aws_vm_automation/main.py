from aws_vm_automation.ec2 import (
    find_latest_ubuntu_ami,
    create_instance,
    get_public_ip,
    terminate_instance,
    wait_until_running,
)

REGION = "eu-central-1"
KEY_NAME = "jr-key"


def main():
    ami = find_latest_ubuntu_ami(REGION)
    print("Latest Ubuntu AMI:", ami)

    print("Creating EC2 instance...")
    instance_id = create_instance(region=REGION, key_name=KEY_NAME)
    print("InstanceId:", instance_id)

    print("Waiting until running...")
    wait_until_running(region=REGION, instance_id=instance_id)

    ip = get_public_ip(region=REGION, instance_id=instance_id)
    print("Public IP:", ip)

    print("Terminating instance...")
    terminate_instance(region=REGION, instance_id=instance_id)
    print("Done.")


if __name__ == "__main__":
    main()