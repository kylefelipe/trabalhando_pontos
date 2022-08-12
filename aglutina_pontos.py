from qgis.core import (QgsGeometry, QgsPoint, QgsLineString, QgsProject)
from qgis.core import QgsVectorFileWriter


def montaPonto(x, y):
    return QgsPoint(x, y)


def monta_linha(pontos):
    linha = QgsLineStrings(pontos)
    return linha