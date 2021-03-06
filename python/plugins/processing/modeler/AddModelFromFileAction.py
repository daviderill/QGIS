# -*- coding: utf-8 -*-

"""
***************************************************************************
    EditScriptAction.py
    ---------------------
    Date                 : August 2012
    Copyright            : (C) 2012 by Victor Olaya
    Email                : volayaf at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Victor Olaya'
__date__ = 'April 2014'
__copyright__ = '(C) 201, Victor Olaya'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os
import shutil
from PyQt4 import QtGui
from processing.gui.ToolboxAction import ToolboxAction
from processing.modeler.ModelerAlgorithm import ModelerAlgorithm
from processing.modeler.WrongModelException import WrongModelException
from processing.modeler.ModelerUtils import ModelerUtils

class AddModelFromFileAction(ToolboxAction):

    def __init__(self):
        self.name = "Add model from file"
        self.group = 'Tools'

    def getIcon(self):
        return QtGui.QIcon(os.path.dirname(__file__) + '/../images/model.png')

    def execute(self):
        filename = QtGui.QFileDialog.getOpenFileName(self.toolbox, 'model files', None,
                '*.model')
        if filename:
            try:
                ModelerAlgorithm.fromFile(filename)
            except WrongModelException:
                QtGui.QMessageBox.warning(self.toolbox, "Error reading model", "The selected file does not contain a valid model")
                return
            except:
                QtGui.QMessageBox.warning(self.toolbox, "Error reading model", "Cannot read file")
            destFilename = os.path.join(ModelerUtils.modelsFolder(), os.path.basename(filename))
            shutil.copyfile(filename,destFilename)
            self.toolbox.updateProvider('script')