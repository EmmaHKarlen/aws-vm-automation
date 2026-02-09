# AWS VM Automation (EC2) — Python
A personal project that automates provisioning and cleanup of AWS EC2 instances using Python (boto3).
Built as a junior-friendly DevOps/Backend automation project with a focus on clean structure, safe defaults, and reproducible steps.


## Features (planned / in progress)
- Resolve the latest Ubuntu 22.04 AMI per region automatically
- Create an EC2 instance with tags (Project/Owner)
- Print instance status + public IPv4
- Terminate instance (cleanup)
- (Optional) Create a Security Group that allows SSH only from the user's public IP
- Persist state locally (`state.json`) to enable one-command cleanup
- Dry-run mode (no resources created)

## Requirements
- Python 3.10+
- AWS account (Free Tier is enough)
- AWS credentials configured locally (`aws configure`)
- IAM user with permission to manage EC2 (for learning, `AmazonEC2FullAccess` is OK)

## Setup
python -m venv .venv
# Windows:
.venv\Scripts\activate
pip install -r requirements.txt

## Configure AWS credentials
aws configure
Region example: eu-central-1

## Safety notes
- Never commit secrets or SSH keys
- .gitignore excludes .env and *.pem
- Always terminate instances after testing

## Project structure
aws-vm-automation/
  src/aws_vm_automation/
  tests/
  README.md
  requirements.txt