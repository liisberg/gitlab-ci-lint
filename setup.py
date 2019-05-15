from setuptools import setup

setup(
    name="gitlab-ci-lint",
    version="1.0",
    description="Command line tool to validate a .gitlab-ci.yml file",
    author="Christian Liisberg",
    url="https://github.com/liisberg/gitlab-ci-lint",
    license="MIT",
    packages=["gitlab_ci_lint"],
    install_requires=[
        "click",
        "requests",
    ],
    entry_points = {
        "console_scripts": ["gitlab-ci-lint=gitlab_ci_lint.cli:cli"],
    }
)

