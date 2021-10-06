import argparse
import pathlib
import wandb
from logger import setup_logger

log = setup_logger(__name__,"use_artifact.log")


def go(args):
    log.info("Creating run in project exercise_1")
    run = wandb.init(project="exercise_1", job_type="use_file")

    log.info("Getting artifact")

    # YOUR CODE HERE: get the artifact and store its local path in the variable "artifact_path"
    # HINT: you can get the artifact path by using the "file()" method
    artifact = run.use_artifact(args.artifact_name)

    artifact_path = artifact.file()

    log.info("Artifact content:")
    with open(artifact_path, "r") as fp:
        content = fp.read()

    print(content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Use an artifact from W&B", fromfile_prefix_chars="@"
    )

    parser.add_argument(
        "--artifact_name", type=str, help="Name and version of W&B artifact", required=True
    )

    args = parser.parse_args()

    go(args)