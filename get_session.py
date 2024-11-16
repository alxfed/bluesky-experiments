# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from datetime import datetime, timezone
from os import getenv
import requests
pds_url = 'https://bsky.social'

headers = {'Content-Type': 'application/json'}

data = {
    "identifier": getenv('BLUESKY_HANDLE'),
    "password": getenv('BLUESKY_PASSWORD')
}

response = requests.post(
    url=pds_url + '/xrpc/com.atproto.server.createSession',
    headers=headers,
    json=data
)
res = response.json()
ACCESS_JWT = res['accessJwt']
REFRESH_JWT = res['refreshJwt']

now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

create_post_data = {
    "repo": getenv("BLUESKY_HANDLE"),
    "collection": "app.bsky.feed.post",
    "record":
            {
                "text": "Hello world! I posted this via the REST API and Requests library. It's pretty simple.",
                "createdAt": now
            }
    }

auth_headers = {
    "Authorization": "Bearer " + ACCESS_JWT,
    "content-type": "application/json"
}
response = requests.post(
    url = pds_url + '/xrpc/com.atproto.repo.createRecord',
    headers = auth_headers,
    json = create_post_data
)

...