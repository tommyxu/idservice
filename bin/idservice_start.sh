#!/bin/bash
gunicorn idservice:app -w 2 -k uvicorn.workers.UvicornWorker
