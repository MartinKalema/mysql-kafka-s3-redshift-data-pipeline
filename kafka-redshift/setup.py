from setuptools import setup,find_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME="redshift-consumer"
VERSION="0.0.3"
AUTHOR="Martin Kalema"
DESRCIPTION="This is pyspark mysql kafka pipeline"




setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESRCIPTION,
packages=find_packages(), 
)