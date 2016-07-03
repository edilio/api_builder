#!/usr/bin/env python

import os
import sys

APP_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)))
BASE_DIR = os.path.dirname(APP_DIR)
print APP_DIR
print BASE_DIR

print '='*90

sys.path.append(APP_DIR)
sys.path.append(BASE_DIR)
#
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_builder.settings')

import django
django.setup()

from django.db.models import Q
from mezzanine.generic.models import ThreadedComment


def delete_sex_pill_comments():
    qs_filter = Q()
    bad = ['levitra', 'cialis', 'viagra', 'prescription', 'buy', 'cheap', 'erectile', 'dysfuntion']
    for b in bad:
        qs_filter |= Q(comment__contains=b)
    ThreadedComment.objects.filter(qs_filter).delete()


def main():
    delete_sex_pill_comments()

if __name__ == '__main__':
    main()
