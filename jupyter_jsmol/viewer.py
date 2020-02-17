import ipywidgets as widgets
from traitlets import Unicode, Dict


# See js/lib/viewer.js for the frontend counterpart to this file.

@widgets.register
class JsmolView(widgets.DOMWidget):
    """An example widget."""

    # Name of the widget view class in front-end
    _view_name = Unicode('JsmolView').tag(sync=True)

    # Name of the widget model class in front-end
    _model_name = Unicode('JsmolModel').tag(sync=True)

    # Name of the front-end module containing widget view
    _view_module = Unicode('jupyter-jsmol').tag(sync=True)

    # Name of the front-end module containing widget model
    _model_module = Unicode('jupyter-jsmol').tag(sync=True)

    # Version of the front-end module containing widget view
    _view_module_version = Unicode('^0.1.0').tag(sync=True)
    # Version of the front-end module containing widget model
    _model_module_version = Unicode('^0.1.0').tag(sync=True)

    # Widget specific property.
    # Widget properties are defined as traitlets. Any property tagged with `sync=True`
    # is automatically synced to the frontend *any* time it changes in Python.
    # It is synced back to Python from the frontend *any* time the model is touched.

    info = Dict(help="The values for initialising the jmol applet").tag(sync=True)
    cmd = Unicode(help="The commands for jmol applet").tag(sync=True)

    def __init__(self, width="100%", height=400, color="gray", script='', **kwargs):
        super().__init__(**kwargs)
        self.info = {
            'width': width,
            'height': height,
            'color': color,
            'script': script,
            'use': "HTML5",
            'j2sPath': "/nbextensions/jupyter-jsmol/j2s",
            'antialiasDisplay': True,
            'disableInitialConsole': True,
            'disableJ2SLoadMonitor': True,
            'debug': False,
        }

    def script(self, cmd):
        # TODO: it should be only one directional
        self.cmd = cmd
