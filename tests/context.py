import os
import sys

# Adds "eve" to sys.path
# Now you can do import with "from eve.Sub-Package ..."
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "eve"))
)
