#!/bin/sh
gunicorn server:app --bind 0.0.0.0:3000 --workers=3