# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='groupspace.roles',
      version=version,
      description="A roles tab for assigning dynamic local roles",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='GrufSpaces, GroupSpace, Roles, PAS, borg.localrole',
      author='Maik Röder',
      author_email='roeder@berg.net',
      url='https://svn.plone.org/svn/collective/groupspace.roles',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['groupspace'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [distutils.setup_keywords]
      paster_plugins = setuptools.dist:assert_string_list

      [egg_info.writers]
      paster_plugins.txt = setuptools.command.egg_info:write_arg
      """,
      paster_plugins = ["ZopeSkel"],
      )