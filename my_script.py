import argparse
from logger import setup_logger
log = setup_logger(__name__,"my_script.log")

def go(args):
    # Your code here
    # For example:
    log.info(args)
    log.info("This is a message")
    log.warning("This is a warning")
    log.error("This is an error")

    log.info(f"This is {args.artifact_name}")

    log.info(f"This is {args.optional_arg}")

if __name__ == "__main__":
    # This block is executed only if this file is being
    # executed as a script. It is NOT executed if the file
    # is imported as a module
    parser = argparse.ArgumentParser(
        description="This is a tutorial on argparse"
    )

    parser.add_argument(
        "--artifact_name", type=str, help="Name and version of W&B artifact", required=True
    )

    parser.add_argument(
        "--optional_arg", type=float, help="An optional argument", required=False,
        default=2.3
    )

    args = parser.parse_args()

    go(args)
