# autogenerated by __main__.py do not edit
top_level_module_names=('QtCore', 'QtGui', 'QtWidgets', 'QtNetwork', 'QtSvg', 'QtPrintSupport', 'QtOpenGL', 'QtOpenGLWidgets', 'QtQuick', 'QtWebEngineCore', 'QtWebEngineWidgets', 'QtDBus')


def __getattr__(name):
    if name in top_level_module_names:
        import importlib
        return importlib.import_module("PyQt6." + name)
    raise AttributeError(name)

