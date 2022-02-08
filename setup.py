from setuptools import setup

import pystontest
extension = pystontest.ffi.verifier.get_extension()

setup(
	name='pystontest',
	packages=['pystontest'],
	ext_modules=[extension],
	install_requires=['cffi'],
	setup_requires=['setuptools_scm', 'cffi'],
)
