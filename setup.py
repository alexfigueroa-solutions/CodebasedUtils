from setuptools import setup, find_packages

setup(
    name="codespace-utils",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'click',
        'colorama'
    ],
    entry_points={
    'console_scripts': [
        'util=codespace_utils.print_dir:util',
    ],

}

)
