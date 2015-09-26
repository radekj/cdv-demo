from setuptools import setup, find_packages
version = '0.1'

setup(name='cdv',
      version=version,
      description="Demo project",
      packages=find_packages(),
      install_requires=[
          'setuptools',
          'collective.folderishtypes',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
