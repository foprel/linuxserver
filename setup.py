from setuptools import setup


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='linuxserver',
    version='0.0.1',
    description='A simple CLI to deploy linuxserver services',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Frank Oprel',
    author_email='fj.oprel@gmail.com',
    url='https://github.com/foprel/linuxserver',
    install_requires=requirements,
    license=license,
    packages=['.'],
    include_package_data=True,
    entry_points={
        'console_scripts': ['cinema = cli:main'],
    },
    python_requires='>=3.8',
)