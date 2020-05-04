# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import os

import pytest

from datadog_checks.dev import docker_run

from .common import CHECK_CONFIG, HERE, API_URL, USERNAME, PASSWORD


@pytest.fixture(scope="session")
def dd_environment():
    with docker_run(compose_file=os.path.join(HERE, 'compose', 'docker-compose.yml'),):
        yield CHECK_CONFIG


@pytest.fixture
def instance():
    return {
        'url': API_URL,
        'username': USERNAME,
        'password': PASSWORD,
        'auth_type': 'digest',
    }
