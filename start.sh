#!/bin/sh
gunicorn server:app --bind 0.0.0.0:5000 --workers=3
