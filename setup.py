import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-coturn',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='A django app to sync users between django and a coturn server',
    long_description=README,
    url='https://github.com/kingandunion.com/django-coturn',
    author='Aaron Gee-Clough',
    author_email='aaron@kingandunion.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    keywords = "django coturn webrtc",
    install_requires=['django'],
    python_requires=">=3"
)
