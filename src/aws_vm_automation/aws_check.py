import boto3


def check_aws_connection():
    sts = boto3.client("sts")
    identity = sts.get_caller_identity()
    return identity


def main():
    identity = check_aws_connection()
    print("Connected to AWS successfully:")
    print(identity)


if __name__ == "__main__":
    main()
