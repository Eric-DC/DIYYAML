#!/bin/python3 

#Class dedicated to handling load
import yaml


__author__ = 'Eric'
class geoload():


    def __init__(self, path, auth=None, **kwargs):
        self.path = 'spec.yaml'

    def loadfile(path):
        with open(path, 'r') as file:
        	return file.read()

    def yaml_to_dict(str):
    	return yaml.safe_load(str)
    	



