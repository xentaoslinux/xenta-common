#!/usr/bin/python2

import os
import gettext

gettext.install("xenta-common", "/usr/share/xentaos/locale")

if os.path.exists("/usr/bin/gksu"):
    launcher = "gksu  --message \"<b>" + _("Please enter your password") + "</b>\""
elif os.path.exists("/usr/bin/kdesudo"):
    launcher = "kdesudo -i /usr/share/xentaos/logo.png -d --comment \"<b>" + _("Please enter your password") + "</b>\""

print (launcher)
