from setuptools import setup, find_packages

from wagtailshowsimilar import __version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="wagtail-showsimilar",
    version=__version__,
    author="ongchi",
    author_email="ongchi@users.noreply.github.com",
    description="wagtail input panel",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ongchi/wagtail-showsimilar",
    project_urls={
        "Bug Tracker": "https://github.com/ongchi/wagtail-showsimilar/issues",
    },
    install_requires=['wagtail>=2.3'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Wagtail',
        'Framework :: Wagtail :: 2',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.6",
)
