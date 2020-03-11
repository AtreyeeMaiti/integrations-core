# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import csv
import os
import sys
import warnings

E2E_PARENT_PYTHON = 'DDEV_E2E_PYTHON_PATH'
CI_WARNING_PREFIX = '##vso[task.logissue type=warning] '


def e2e_testing():
    return E2E_PARENT_PYTHON in os.environ


def running_on_ci():
    return 'SYSTEM_TEAMFOUNDATIONCOLLECTIONURI' in os.environ


def get_check_root_path():
    return sys.argv[0].split('.tox')[0]


def get_metadata_metrics():
    metadata_path = os.path.join(get_check_root_path(), 'metadata.csv')
    metrics = {}
    with open(metadata_path) as f:
        for row in csv.DictReader(f):
            metrics[row['metric_name']] = row
    return metrics


def echo_warning(msg):
    if running_on_ci():
        msg = "{} {}".format(CI_WARNING_PREFIX, msg)
    warnings.warn(msg)