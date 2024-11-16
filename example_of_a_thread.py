# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from atproto import Client, client_utils, models
from os import getenv


def main():
    client = Client()
    # handle is without @
    profile = client.login(
        login=getenv('BLUESKY_HANDLE'),
        password=getenv('BLUESKY_PASSWORD')
    )
    # print('Welcome,', profile.display_name)

    text = client_utils.TextBuilder().text("Example thread. This is the initial post.")
    post = client.send_post(text)

    resp_model =models.utils.get_response_model(response=post)

    parent = models.create_strong_ref(post)
    root = models.create_strong_ref(post)

    reply_to_root = client.send_post(
        text='This is a reply to a root post of the thread.',
        reply_to=models.AppBskyFeedPost.ReplyRef(parent=parent, root=root)
    )

    reply = models.create_strong_ref(reply_to_root)
    reply_to_reply = client.send_post(
        text='This is a reply to a reply of the thread.',
        reply_to=models.AppBskyFeedPost.ReplyRef(parent=reply, root=root)
    )
    ...


if __name__ == '__main__':
    main()