# RevKit: A Toolkit for Reversible Circuit Design (www.revkit.org)
# Copyright (C) 2009-2011  The RevKit Developers <revkit@informatik.uni-bremen.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import QIcon, QTreeWidget, QTreeWidgetItem

class MessagesWidget( QTreeWidget ):
    message_added = pyqtSignal()

    def __init__( self, parent = None ):
        QTreeWidget.__init__( self, parent )

        self.setHeaderLabels( [ "Message", "Sender" ] )
        self.setRootIsDecorated( False )
        self.setColumnWidth( 0, 700 )

    def addMessage( self, message, sender, icon = "information" ):
        item = QTreeWidgetItem( [ message, sender ] );
        item.setIcon( 0, QIcon.fromTheme( "dialog-" + icon ) )
        self.addTopLevelItem( item )
        self.message_added.emit()

