# configcompare:

  This file will compare two YAML files, where --file1 is the developers configuration
file that does not get checked into GIT. The other YAML file, --file2, will be
the sample configuration file that does get checked into GIT. There is also a directory
parameter, --dir, that is also passed just in-case your config files are in a directory.
If your config files are at the top of the directory structure just pass in blank

## pre-commit
If you want to run it from Github use this configuration
```yaml
 - repo: https://github.com/akocs/configcompare
    rev: main  # The version of the configcompare
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
```
If you want to run it locally use this configuration
```yaml
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
```
