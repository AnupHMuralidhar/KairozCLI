from setuptools import setup, find_packages

setup(
    name="kairoz",
    version="1.0.0",
    description="AI-powered CLI cybersecurity assistant",
    author="Your Name",
    packages=find_packages(include=["kairoz", "kairoz.*"]),
    include_package_data=True,
    install_requires=open("requirements.txt").read().splitlines(),
    entry_points={
        "console_scripts": [
            "kairoz=kairoz.kairoz_cli:entrypoint"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
