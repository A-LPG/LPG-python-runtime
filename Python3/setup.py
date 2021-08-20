from setuptools import setup

setup(
    name='lpg2-python3-runtime',
    version='0.0.1',
    packages=['lpg2'],
    package_dir={'': 'src'},
    install_requires=[
        "typing  python_version<'3.5'",
    ],
    url='https:/github.com/A-LPG/LPG-python-runtime',
    license='MIT',
    author='Kuafuwang',
    author_email='731784510@qq.com',
    description='Python3  runtime for LPG2'
)
