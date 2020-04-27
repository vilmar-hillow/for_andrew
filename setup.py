"""
Dotenv script setup.
"""

import setuptools

# fmt: off
CONFIG = {
    "name": "dotenv_script",
    "version": "0.1",
    "description": "Dotenv script.",

    "install_requires": (
        "python-dotenv",
    ),
    "entry_points": {
        "console_scripts": [
            "dotenv_script = dotenv_script.dotenv_script:main",
        ]
    },

    "packages": [*setuptools.find_packages()],
}
# fmt: on


setuptools.setup(**CONFIG)
