from setuptools import setup, find_packages

setup(
    name="codespace_utils",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'click',
        'colorama'
    ],
    entry_points={
    'console_scripts': [
        'util=core.print_dir:util',
    ],

}

)
