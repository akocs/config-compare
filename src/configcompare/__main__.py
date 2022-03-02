#!/usr/bin/env python3
# Copyright 2022 Tony Akocs
# SPDX-License-Identifier: MIT
import argparse
import os
from typing import Sequence

import yaml

"""
This file will compare two YAML files, where --file1 is the developers configuration
file that does not get checked into GIT. The other YAML file, --file2, will be
the sample configuration file that does get checked into GIT. There is also a directory
parameter, --dir, that is also passed just in-case your config files are in a directory.
If your config files are at the top of the directory structure just pass in blank

- repo: https://github.com/akocs/configcompare
    rev: main
    hooks:
      - id: configcompare
        name: configcompare
        description: Compare the projects sample config keys to developers config file
        language: python
        language_version: 3.8.6
        additional_dependencies: [pyyaml]
        args:
          [
            "--dir=deployment",
            "--file1=config.yaml",
            "--file2=config-sample.yaml",
          ]

or to run it locally from the .git/hooks directory

 - repo: local
    hooks:
      - id: configcompare
        name: configcompare
        description: Compare the projects sample config keys to developers config file
        language: python
        language_version: 3.8.6
        additional_dependencies: [pyyaml]
        entry: python .git/hooks/configcompare.py
        args:
          [
            "--dir=deployment",
            "--file1=config.yaml",
            "--file2=config-sample.yaml",
          ]

"""

def __loadConfigFile(directory: str, fileName: str) -> dict:
    # Get current working directory
    cwd = os.getcwd()
    print(f"PATH: {cwd}")
    keys = []
    if directory != "":
        localFileName = cwd + "/" + directory + "/" + fileName
    else:
        localFileName = cwd + "/" + fileName
    with open(localFileName, "r") as stream:
        try:
            data = yaml.safe_load(stream)
            for key in data:
                keys.append(key)
        except yaml.YAMLError as exc:
            print(exc)
    return keys

def __compareList(l1,l2) -> bool:
   l1.sort()
   l2.sort()
   if (l1 == l2):
      return True
   else:
      return False

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--dir', type=str, default='',
        help='directory where the config files are located',
    )
    parser.add_argument(
        '--file1', type=str, default='config.yaml',
        help='Developers config YAML file',
    )
    parser.add_argument(
        '--file2', type=str, default='config-sample.yaml',
        help='Sample config YAML file',
    )
    parser.set_defaults(verbose=False)
    parser.add_argument('files', nargs=argparse.REMAINDER)
    return parser.parse_args()


def main() -> int:
    args = parse_arguments()
    directory = args.dir
    configFile = args.file1
    configSampleFile = args.file2
    configKeys = []
    configSampleKeys = []
    configKeys = __loadConfigFile(directory, configFile)
    configSampleKeys = __loadConfigFile(directory, configSampleFile)

    if (__compareList(configKeys, configSampleKeys)):
        print("Config files are same")
    else:
        print(
            f"Missing values in {configSampleFile} missing:", (
            set(configKeys).difference(configSampleKeys)
            ),
        )
        return 1

if __name__ == '__main__':
    print("IN CONFIG COMPARE")
    raise SystemExit(main())
