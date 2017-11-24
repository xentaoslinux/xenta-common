#!/usr/bin/python2

import os
import gettext
import sys
sys.path.append('/usr/lib/xentaos/common')
import additionalfiles

DOMAIN = "xenta-common"
PATH = "/usr/share/xentaos/locale"

prefix = "[Nemo Action]\n"

suffix = """Exec=thunderbird -compose to=,\"attachment='%F'\"
Icon-Name=mail-attachment
Selection=NotNone
Extensions=nodirs;
Dependencies=thunderbird;
Separator=,
"""

os.environ['LANGUAGE'] = "en_US.UTF-8"
gettext.install(DOMAIN, PATH)
additionalfiles.generate(DOMAIN, PATH, "usr/share/nemo/actions/mint-artwork-cinnamon-thunderbird.nemo_action", prefix, _("Send by Email"), _("Send as email attachment"), suffix)
