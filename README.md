<!--
Copyright 2022 Tony Akocs
SPDX-License-Identifier: MIT
-->
# config-compare

## Backgroud:
If you are on a project where there is a config-sample.yaml file that contains example 
configurations for the project in YAML format. When a developer wants to run the project
they will just copy the config-sample.yaml file and rename it to config.yaml. They can
run the project using their own custom project configurations using  the config.yaml file.
The config-sample.yaml file is always checked in to the repository but the developer's 
custom config.yaml file is never checked into the repository.

When a developer makes a change to the application and adds a new key/value pair to their 
config.yaml file. Sometimes they forget to add it to the config-sample.yaml file. Then
they check all their changes into the repo. You then pull down their changes and build
the application. You will get an error that says something like 'unknown property' or
'property not found' error. 

To solve this, you can use config-compare pre-commit hook.

# Description:
This pre-commit hook will compare two YAML configuration files. It will compare the 
develops custom config.yaml file to the project's config-sample.yaml file. If the 
config-sample.yaml file does not contain a key/value pair that is in the developers
config.yaml file. An error will be thrown. 

## Parameters
| Command Line    | Input                   | Description                                                    |
| --------------- | ----------------------- | -------------------------------------------------------------- |
| --dir           |  String directory name  | Directory that the config files are located if ther is one     |
| --file1         |  String file name       | The developers custom config file (example: config.yaml)       |
| --file2         |  String file name       | The project sample config file (example: config-sample.yaml)   |

## To Run:

```bash
# run in current directory
config-compare
# config-compare --file1 "config.yaml" --file2 "config-sample.yaml"

# run where the config files are in a directory (ex: deployment)
# config-compare --dir "deployment" --file1 "config.yaml" --file2 "config-sample.yaml"
```


## pre-commit
If you want to run it from Github use this configuration
```yaml
 - repo: https://github.com/akocs/config-compare
    rev: main
    hooks:
      - id: config-compare
        additional_dependencies: [pyyaml]
        always_run: true
        args:
          [
            "--dir=deployment",
            "--file1=config.yaml",
            "--file2=config-sample.yaml",
          ]
```

