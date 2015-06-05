from setuptools import find_packages
from setuptools import setup
import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.1-externalvideo'

long_description = (
    read('em', 'skin', 'docs', 'index.rst'))

setup(name='em.skin',
      version=version,
      description="Plumi theme & customizations for engagemedia.org",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Hexagon IT',
      author_email='oss@hexagonit.fi',
      url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['em'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'hexagonit.testing',
          'manuel',
          'plone.app.testing',
          'plone.app.theming',
          'plone.browserlayer',
          'setuptools',
          'unittest2',
          'Products.ContentWellPortlets',
          'zope.i18nmessageid',
	  'quintagroup.dropdownmenu',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
