#!/bin/bash

uvicorn --factory src.main:init_app  --host 0.0.0.0 --port 8000 --proxy-headers --forwarded-allow-ips=* --reload 