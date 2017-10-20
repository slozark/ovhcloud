from setuptools import setup, find_packages

setup(
    name='ovhcloud',

    use_scm_version=True,

    setup_requires=['setuptools_scm==1.15.5'],

    description='A command-line tool for OVH API',
    #long_description=long_description,

    url='https://github.com/slozark/ovhcloud',

    author='Sylvain Devroede',
    author_email='sylvdevr@gmail.com',

    license='GPL3',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='cloud ovh',

    #packages=find_packages(exclude=['tests']),

    package_data={'ovhcloud': ['endpoints_cache.json']},

    install_requires=['ovh==0.4.8'],

    tests_require=['pytest>=3.0.7',
                   'pytest-capturelog>=0.7',
                   'coverage>=4.4.0'],

    include_package_data=True,

    entry_points={
        'console_scripts': [
            'ovhcloud=client:main',
        ],
    },
)