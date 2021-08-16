"""
Metadata
"""

from importlib import metadata

print(metadata.version('pip'))
print(list(metadata.metadata('pip')))
