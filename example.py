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
    # print('Welcome,', profile.display_name)

    text = client_utils.TextBuilder().text("Hello bluesky! I posted and 'liked' this via the Python SDK. ").link('Python SDK', 'https://atproto.blue')
    post = client.send_post(text)
    client.like(post.uri, post.cid)


if __name__ == '__main__':
    main()
