from setuptools import find_packages
from setuptools import setup


setup(
    name='commit_hooks',
    description='Personal hooks',
    url='https://github.com/Sykomaniac/commit-hooks',
    version='0.1.0',

    author='Ashley Sykes',
    author_email='ashleysykes01@gmail.com',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    packages=find_packages(exclude=('tests*', 'testing*')),
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'commit-msg-format = pre_commit_hooks.commit_message_format:main',
            'commit-message = pre_commit_hooks.commit_message:main',
        ],
    },
)
