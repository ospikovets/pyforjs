import setuptools

with open('README.md') as f:
    long_description = f.read()


setuptools.setup(
    name='pyforjs',
    version='0.0.1',
    license='MIT',
    author='Oleksandr Pikovets',
    author_email='ospikovets@gmail.com',
    description='Python library to lint JavaScript',
    long_description=long_description,
    project_urls={
        'Issues Tracker': 'https://github.com/ospikovets/pyforjs/issues',
        'Source Code': 'https://github.com/ospikovets/pyforjs',
    },
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    keywords='JavaScript JS linter',
    classifiers=(
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        'Topic :: Software Development :: Testing',
    ),
    test_suite='nose.collector',
    tests_require=['nose'],
    entry_points={
      'console_scripts': ['pyforjs=pyforjs.command_line:main'],
    },
    include_package_data=True,
    zip_safe=False
)
