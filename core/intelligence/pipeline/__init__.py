# -*- coding: utf-8 -*-
"""
Compatibility shim: upstream used core.intelligence.pipeline.X structure.
Our layout is flat: core.intelligence.X (scripts at top level).
This __init__.py makes `from core.intelligence.pipeline.X import Y` work
by proxying imports to core.intelligence.X.

MCE sub-package lives here: core.intelligence.pipeline.mce/
"""
