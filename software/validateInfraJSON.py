#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 11:39:04 2018

@author: kavisha
"""

#validate infrajson

import json
import jsonschema
#from jsonschema import Draft7Validator
import jsonschema
#import os

filename =  r'/Users/kavisha/Desktop/githubpvt/InfraJSON/sampledata/example_infrajson_corefeatures.json'
#filename =  r'/Users/kavisha/Desktop/githubpvt/InfraJSON/sampledata/example_infrajson_landfeature.json'
schemaname = r'/Users/kavisha/Desktop/githubpvt/InfraJSON/schema/v01/infrajson.json'

fin = open(filename)
data = fin.read()
j = json.loads(data)
#print (j)

fins = open(schemaname)
schema = fins.read()
js = json.loads(schema)
#print js

#print ('file://%s/' % os.path.abspath(os.path.dirname(__file__)) +"cityjson/schema/v07/")
resolver = jsonschema.RefResolver('file:///Users/kavisha/Desktop/githubpvt/InfraJSON/schema/v01/', None)
#print (resolver)
#try:
##    jsonschema.validate(j,js,resolver=resolver)
#    Draft7Validator.check_schema(js)
#    print("Passed derived schema.")
##except Exception as ex:
##    print("Failed derived schema: %s" % ex)
#except jsonschema.ValidationError as e:
#    print ("hi",e.message)
#except jsonschema.SchemaError as e:
#    print ("ho",e)

try:
    jsonschema.validate(j,js,resolver=resolver)
#    Draft7Validator(js,resolver=resolver).validate(j)
    print("Passed derived schema.")
#except Exception as ex:
#    print("Failed derived schema: %s" % ex)
except jsonschema.ValidationError as e:
    print ("hi",e.message)
except jsonschema.SchemaError as e:
    print ("ho",e)
#print (Draft7Validator.check_schema(schema))