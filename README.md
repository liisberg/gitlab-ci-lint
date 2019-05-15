# gitlab-ci-lint
Gitlab-ci cli to validate .gitlab-ci.yml files

## Usage

### Install
```
python3 setup.py install
```

### CLI
```
gitlab-ci-lint --help
Usage: gitlab-ci-lint [OPTIONS]

Options:
  --url TEXT            The url for your gitlab server, e.g:
                        https://gitlab.example.com  [required]
  --filename, --f PATH  Your .gitlab-ci.yml file, e.g .gitlab-ci.yml
                        [required]
  --help                Show this message and exit.

```

#### Example
```
gitlab-ci-lint --url https://gitlab.com .gitlab-ci.yml
```
