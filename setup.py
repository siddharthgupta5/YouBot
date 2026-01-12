from setuptools import find_packages,setup

setup(name="Customer-service-bot",
       description="Customer service bot using langchain and AstraDB",
       version="0.0.1",
       author="Siddharth Gupta",
       author_email="contactsid14@gmail.com",
       packages=find_packages(),
       install_requires=['langchain-astradb','langchain'])