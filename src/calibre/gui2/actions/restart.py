#!/usr/bin/env python


__license__   = 'GPL v3'
__copyright__ = '2010, Kovid Goyal <kovid@kovidgoyal.net>'
__docformat__ = 'restructuredtext en'


from calibre.gui2.actions import InterfaceAction


class RestartAction(InterfaceAction):

    name = 'Restart'
    action_spec = (_('Restart'), 'restart.png', _('Restart calibre'), 'Ctrl+R')

    def genesis(self):
        self.qaction.triggered.connect(self.restart)

    def restart(self, *args):
        self.gui.quit(restart=True)
