from setuptools import setup

setup(
    name='ipython-run-sync',
    version='1.0.0',
    description='Automatically run returned Futures synchronously in ipython',
    url='https://github.com/grantpatten/ipython-run-sync',
    author='grantpatten',
    requires=[
        'tornado'
    ],
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    py_modules=['run_sync']
)
