#!/bin/bash

uvicorn --factory src.app.main:init_app --reload