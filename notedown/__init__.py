from .notedown import *  # noqa: F403
from .main import (
    convert as convert,
    markdown_template as markdown_template,
    __version__ as __version__,
)

# avoid having to require the notebook to install notedown
try:
    from .contentsmanager import NotedownContentsManager
    from .contentsmanager import NotedownContentsManagerStripped
except ImportError:
    err = "You need to install the jupyter notebook."
    NotedownContentsManager = err
    NotedownContentsManagerStripped = err
