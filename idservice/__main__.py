import sys
from uvicorn.main import main as uvicorn_main


def main():
    args = "idservice.api:app --no-access-log --loop uvloop".split(" ")
    sys.argv.extend(args)
    sys.exit(uvicorn_main())


if __name__ == "__main__":
    main()
