#! /usr/bin/env python

from argparse import ArgumentParser
import importlib
import sys
import ast
import os
from subprocess import call

def _getAppModule():
    try:
        return importlib.import_module(args.module)
    except:
        print >> sys.stderr, 'Cannot find module ' + args.module;
        exit()

def _getFileDictionary(file_dictionary_string):
    result = {}
    # If we have multiple ports we should have a string representation of a
    # python dictionary. Otherwise we have a single path string.
    try:
        dictionary_literal = file_dictionary_string.replace('{',"{\'").replace(':',"\':\'").replace(',',"\',\'").replace('}',"\'}")
        result = ast.literal_eval(dictionary_literal)
    except:
        result[''] = file_dictionary_string
    return result

def _checkInputFileDict(input_files_dict):
    # Check that all the files exist
    for port, filename in input_files_dict.items():
        if not os.path.isfile(filename):
            print >> sys.stderr, 'Input file "' + filename + '" not found (port ' + port +')'
            exit()

def _checkOutputFileDict(output_files_dict):
    # If a directory of an output file does not exist create it
    for _, filename in output_files_dict.items():
        out_dir = os.path.abspath(os.path.dirname(filename))
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

if __name__ == '__main__':
    
    parser = ArgumentParser(description='Executes a Euclid Wrapper')
    parser.add_argument('-m', '--module', help='The module with the application specific implementations', required=True)
    parser.add_argument('-i', '--input', help='The Euclid DM XML input files', required = True)
    parser.add_argument('-o', '--output', help='The Euclid DM XML output files', required = True)
    args = parser.parse_args()
    
    # Load the module which contains all the application specific information
    app_module = _getAppModule();
    
    # Build the command to execute
    exec_command = []
    exec_command.append(app_module.getApplicationName())
    
    # Get the input and output Euclid XML files in directory format
    input_files_dict = _getFileDictionary(args.input)
    _checkInputFileDict(input_files_dict)
    output_files_dict = _getFileDictionary(args.output)
    _checkOutputFileDict(output_files_dict)
    
    # Generate the command to execute
    try:
        exec_command.extend(app_module.generateCommandParameters(input_files_dict, output_files_dict))
    except Exception as ex:
        print >> sys.stderr, ex
        exit()
    
    print >> sys.stderr, "Executing command:"
    print >> sys.stderr, ' '.join(exec_command)
    call(exec_command)
    
    # Postprocess the results to convert them in the Euclid DM format
    app_module.postProcessOutput(output_files_dict, exec_command)
    print >> sys.stderr, 'Done!'