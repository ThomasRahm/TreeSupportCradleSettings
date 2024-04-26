import platform

from . import CuraEngineCradleSettings

from UM.i18n import i18nCatalog
catalog = i18nCatalog("cura")

def getMetaData():
    return {}

def register(app):
    return { "backend_plugin": CuraEngineCradleSettings.CuraEngineCradleSettings() }