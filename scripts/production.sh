#!/bin/bash
gunicorn idservice:app -w 4 -k uvicorn.workers.UvicornWorker
