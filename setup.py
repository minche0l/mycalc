import setuptools

setuptools.setup (
  include_package_data = True,
  name='mycalc'
  version ='0.0.1',
  description ='oss-dev my calc'
  author ='mincheolkim',
  author-email ='kio7543@naver.com',
  url = "https://github.com/minche0l/mycalc/new/main",
  downloadurl = "https://github.com/minche0l/mycalc/releases/tag/v1.0.0.zip",
  install_requires=['pytest'],
  long_description = 'oss-dev calculator python module',
  long_description_content_type='text/markdown',
  classifiers=[
    "programminf language :: python :: 3",
    "Operating System :: OS Independent",
  ],
)
