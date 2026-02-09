from aws_vm_automation.ec2 import find_latest_ubuntu_ami

if __name__ == "__main__":
    ami = find_latest_ubuntu_ami("eu-central-1")
    print("Latest Ubuntu AMI:", ami)
