# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CortarBuffer
                                 A QGIS plugin
 Calculo de extensão de vias dentro de um determinado buffer ao redor de vários pontos.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-06-26
        copyright            : (C) 2024 by R. A. Szeliga
        email                : rafaelsz@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load CortarBuffer class from file CortarBuffer.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .CortarBuffer import CortarBuffer
    return CortarBuffer(iface)
