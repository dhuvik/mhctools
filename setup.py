# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import logging
import re

from setuptools import setup

readme_dir = os.path.dirname(__file__)
readme_filename = os.path.join(readme_dir, 'README.md')

try:
    with open(readme_filename, 'r') as f:
        readme_markdown = f.read()
except:
    logging.warn("Failed to load %s" % readme_filename)
    readme_markdown = ""

with open('mhctools/__init__.py', 'r') as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        f.read(),
        re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

if __name__ == '__main__':
    setup(
        name='mhctools',
        version=version,
        description="Python interface to running command-line and web-based MHC binding predictors",
        author="Alex Rubinsteyn, Julia Kodysh, Tim O'Donnell",
        author_email="alex@openvax.org, julia@openvax.org, tim@openvax.org",
        url="https://github.com/openvax/mhctools",
        license="http://www.apache.org/licenses/LICENSE-2.0.html",
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Operating System :: OS Independent',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering :: Bio-Informatics',
        ],
        install_requires=[
            'numpy>=1.7',
            'pandas>=0.13.1',
            'varcode>=0.5.9',
            'pyensembl>=1.0.3',
            'sercol>=0.0.2',
            'mhcflurry>=2.0.0',
            'mhcnames>=0.3.2',
        ],
        long_description=readme_markdown,
        long_description_content_type="text/markdown",
        packages=['mhctools', 'mhctools.cli'],
        package_data={
            'mhctools.cli': ['logging.conf'],
            'mhctools': ['logging.conf']},
        entry_points={
            'console_scripts': [
                'mhctools = mhctools.cli.script:main'
            ]
        }
    )
