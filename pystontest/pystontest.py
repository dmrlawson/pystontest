import cffi
import os

ROOT = os.path.abspath(os.path.join(__file__, '..', '..'))
old_cwd = os.getcwd()
os.chdir(ROOT) # so that we can use realtive paths when building the cffi extension

ffi = cffi.FFI()
ffi.cdef("""
	void hello(void);
""")

lib = ffi.verify(
    """
    #include "pystontest/pystontest.h"
    """,
    include_dirs=['.'],
    sources=["pystontest/pystontest.c"]
)

os.chdir(old_cwd)

hello = lib.hello
