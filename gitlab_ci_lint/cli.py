import click
import yaml
import json
import requests

@click.command()
@click.option("--url", required=True, help="The url for your gitlab server, e.g: https://gitlab.example.com")
@click.option("--filename", "--f", required=True, help="Your .gitlab-ci.yml file, e.g .gitlab-ci.yml", type=click.Path(exists=True, readable=True), nargs=1)
def cli(url, filename):

    if "://" not in url:
        exit("URL {} does not look right".format(url))

    proto, host = url.split("://")
    api_url = "{}://{}/api/v4/ci/lint".format(proto, host)

    data = {}
    with open(filename) as f:
        y = yaml.safe_load(f)
        data["content"] = json.dumps(y)

    rv = None
    try:
        r = requests.post(api_url, headers={"Content-Type": "application/json"}, json=data, timeout=1.0)
        r.raise_for_status()
        rv = r.json()
    except requests.exceptions.HTTPError as err:
        exit("Error: {}".format(str(err)))

    return click.echo(rv)


if __name__ == "__main__":
    cli()
