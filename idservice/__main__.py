import sys
import subprocess
from uvicorn.main import main


def start():
    args = "idservice.api:app --no-access-log --loop uvloop".split(" ")
    sys.argv.extend(args)
    main()


if __name__ == "__main__":
    start()
