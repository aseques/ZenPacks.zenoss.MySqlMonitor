###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2007, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################

import Globals
from Products.ZenModel.migrate.Migrate import Version
from ZenPacks.zenoss.MySqlMonitor import ZenPack
import logging

class BaseClass:
    version = Version(2, 0, 1)

    def migrate(self, pack):
        if pack.__class__ != ZenPack:
            pack.__class__ = ZenPack
