from __future__ import print_function as _

import os as _os
import sys as _sys
import json

import dash as _dash

# noinspection PyUnresolvedReferences
from ._imports_ import *
from ._imports_ import __all__

if not hasattr(_dash, "development"):
    print(
        "Dash was not successfully imported. "
        "Make sure you don't have a file "
        'named \n"dash.py" in your current directory.',
        file=_sys.stderr,
    )
    _sys.exit(1)

_basepath = _os.path.dirname(__file__)
_filepath = _os.path.abspath(_os.path.join(_basepath, "package-info.json"))
with open(_filepath) as f:
    package = json.load(f)

package_name = package["name"].replace(" ", "_").replace("-", "_")
__version__ = package["version"]

_current_path = _os.path.dirname(_os.path.abspath(__file__))

_this_module = _sys.modules[__name__]


_js_dist = [
    {
        "relative_package_path": "dash_split_pane.min.js",
        "external_url": "https://unpkg.com/{0}@{2}/{1}/{1}.min.js".format(
            package_name, __name__, __version__
        ),
        "namespace": package_name,
    },
    {
        "relative_package_path": "dash_split_pane.min.js.map",
        "external_url": "https://unpkg.com/{0}@{2}/{1}/{1}.min.js.map".format(
            package_name, __name__, __version__
        ),
        "namespace": package_name,
    },
]

_css_dist = [
    {
        "relative_package_path": "dash_split_pane.css",
        "external_url": "https://unpkg.com/{0}@{2}/{1}/{1}.css".format(
            package_name, __name__, __version__
        ),
        "namespace": package_name,
    }
]


for _component in __all__:
    setattr(locals()[_component], "_js_dist", _js_dist)
    setattr(locals()[_component], "_css_dist", _css_dist)