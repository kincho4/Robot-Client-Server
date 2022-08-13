from email.policy import default
import json
import argparse

parser = argparse.ArgumentParser(description="Options for settings")
parser.add_argument("-m","--mode", type=str, metavar="", required=True, help="Select mode. create/edit")
parser.add_argument("-d", "--default", action="store_true", help="Default config")
args = parser.parse_args()

default = {
    
}

if args.mode == "create":
    pass
elif args.mode == "edit":
    pass
elif args.mode == "default":
    warning_default = input("Are you sure you want to make a file with default config. If you have existing files they will be reset to default.")
else:
    print(f"{args.mode} is not a valid option. args.mode accepts only create/edit")

