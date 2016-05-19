#!/bin/bash
JENKINS_URL=1 ./manage.py test --nomigrations -- $1