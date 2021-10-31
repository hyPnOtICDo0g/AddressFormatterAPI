#!/bin/bash

gunicorn -w 3 --threads 3 server:app -b 0.0.0.0:$PORT