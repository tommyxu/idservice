from uvicorn.main import main
import sys

if __name__ == "__main__":
    # uvicorn.run("idservice:app", host="127.0.0.1", port=8000, log_level="info")
    #   --env-file PATH                 Environment configuration file.
    sys.argv.append('idservice:app')
    main()