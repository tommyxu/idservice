import sys
from gunicorn.app.wsgiapp import run
from pathlib import Path


def main():
    package_name = Path(__file__).parent.name
    args = (f"-k uvicorn.workers.UvicornWorker {package_name}.api:app").split(" ")
    sys.argv.extend(args)
    sys.exit(run())


if __name__ == "__main__":
    main()
