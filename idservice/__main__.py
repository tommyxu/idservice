import sys
import subprocess
from uvicorn.main import main

if __name__ == "__main__":
    args = "idservice:app --no-access-log --loop uvloop".split(" ")
    sys.argv.extend(args)
    main()
