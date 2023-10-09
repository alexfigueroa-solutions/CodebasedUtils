from setuptools import setup

setup(
    name="codespace-utils",
    version="0.1",
    py_modules=["codespace_utils"],
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        codespace-utils=codespace_utils:main
    ''',
)
