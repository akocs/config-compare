<!--
Copyright 2022 Tony Akocs
SPDX-License-Identifier: MIT
-->
# config-compare
This pre-commit hook prevents commits when the specified YAML files contain different key values.

## Background:
If you're working on a project with a config-sample.yaml file that contains YAML-formatted
example configurations for the project. When a developer wants to run the project,
they just copy and change the config-sample.yaml file to config.yaml. They can use
the config.yaml file to build the project with their own specific project configurations.
The developer's custom config.yaml file is never checked into the repository, 
but the config-sample.yaml file is always checked into the repository.

When a developer makes an application change and updates the config.yaml file with a 
new key value. They often neglect to include it in the config-sample.yaml file. 
Following that, they commit all of their changes to the repository. Then you pull 
down their changes and build the application. You will get an error message that says 
"unknown property" or "property not found".

# Description:
This pre-commit hook will compare two YAML configuration files. It will compare the 
develops custom config.yaml file to the project's config-sample.yaml file. If the 
config-sample.yaml file does not contain a key value that is in the developers
config.yaml file. An error will be thrown. 

## Parameters
| Command Line    | Input                   | Description                                                    |
| --------------- | ----------------------- | -------------------------------------------------------------- |
| --dir           |  String directory name  | (optional) Directory that the config files are located (ex: deployment or code/deployment) |
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

