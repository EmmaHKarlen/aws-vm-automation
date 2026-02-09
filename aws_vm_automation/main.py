import argparse
from aws_vm_automation.ec2 import (
    create_instance,
    get_public_ip,
    terminate_instance,
    wait_until_running,
)

REGION = "eu-central-1"
KEY_NAME = "jr-key"


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="aws-vm-automation")
    p.add_argument("--region", default=REGION, help="AWS region (default: eu-central-1)")
    p.add_argument("--key-name", default=KEY_NAME, help="EC2 key pair name (default: jr-key)")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("create", help="Create an EC2 instance")
    st = sub.add_parser("status", help="Show instance public IP (requires --instance-id)")
    st.add_argument("--instance-id", required=True)

    d = sub.add_parser("destroy", help="Terminate an EC2 instance (requires --instance-id)")
    d.add_argument("--instance-id", required=True)

    return p


def main() -> None:
    args = build_parser().parse_args()
    region = args.region

    if args.cmd == "create":
        print("Creating EC2 instance...")
        instance_id = create_instance(region=region, key_name=args.key_name)
        print("InstanceId:", instance_id)

        print("Waiting until running...")
        wait_until_running(region=region, instance_id=instance_id)

        ip = get_public_ip(region=region, instance_id=instance_id)
        print("Public IP:", ip)

        print("Done. (Remember to destroy it when finished.)")

    elif args.cmd == "status":
        ip = get_public_ip(region=region, instance_id=args.instance_id)
        print("Public IP:", ip)

    elif args.cmd == "destroy":
        print("Terminating instance...")
        terminate_instance(region=region, instance_id=args.instance_id)
        print("Done.")


if __name__ == "__main__":
    main()
