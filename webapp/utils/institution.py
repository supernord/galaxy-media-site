"""Validate against institutions."""

import os
import json
import re
from django.conf import settings

DOMAIN_LIST_PATH = os.path.join(
    settings.BASE_DIR,
    'utils/data/domains.json',
)
INSTITUTION_LIST_PATH = os.path.join(
    settings.BASE_DIR,
    'utils/data/institutions.json',
)


def is_institution_email(email):
    """Return True if given address is for valid institution.

    Match against exact domain and also root domains.
    e.g. if 'uq.edu.au' is a listed domain, then 'blah.uq.edu.au' will also
    return True.
    """
    if not _is_valid_email(email):
        raise ValueError(f"'{email}' is not a valid email address")
    domain = email.split('@')[1]
    # For me@abc.xyz.edu.au, check also root domains xyz.edu.au, edu.au
    possible_root_domains = {
        '@' + '.'.join(domain.split('.')[i:])
        for i in range(len(domain.split('.')) - 1)
    }

    # Hard-check against all email domains
    valid_domains = [
        d.replace('*.', '@')  # All matched against root domains anyway
        for d in get_domains()
    ]
    matching_domains = set(valid_domains) & possible_root_domains
    if matching_domains:
        return True

    # Check against wildcard domains
    wildcard_domain_matches = [
        d.replace('*', '.')
        for d in valid_domains
        if '*' in d
        and re.match(d.replace('*', '.+'), domain)
    ]
    if wildcard_domain_matches:
        return True
    return False


def _is_valid_email(email):
    """Return True if given address is valid."""
    return re.match(r'^[^@]+@[^@]+\.[^@]+$', email)


def get_domains():
    """Return dictionary of domains mapped to institution names."""
    with open(DOMAIN_LIST_PATH) as f:
        return json.load(f)


def get_institution_list():
    """Return list of institutions with name and email domains."""
    with open(INSTITUTION_LIST_PATH) as f:
        institutions = json.load(f)
        institutions.sort(key=lambda i: i['name'])
        return institutions
