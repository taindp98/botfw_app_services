#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "7a659139-2131-4816-ac7a-567072f2ffa7")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
