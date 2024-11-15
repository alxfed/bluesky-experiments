# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from atproto import Client, client_utils
from os import getenv


def main():
    client = Client()
    # handle is without @
    profile = client.login(
        login=getenv('BLUESKY_HANDLE'),
        password=getenv('BLUESKY_PASSWORD')
    )

    # Get profile's posts. Use pagination (cursor + limit) to fetch all
    profile_feed = client.get_author_feed(
        actor=getenv('BLUESKY_ACTOR'),
        filter='posts_and_author_threads',
        limit=30
    )
    for feed_view in profile_feed.feed:
        print('-', feed_view.post.record.text)
    ...


if __name__ == '__main__':
    main()