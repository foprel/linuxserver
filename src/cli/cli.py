from jinja2 import Template
from version import __version__
from . import config
import argparse
import os
import subprocess


SYSTEM = config.system
SERVICES = config.services.keys()
PATHS = config.paths
DOWNLOADS = PATHS[SYSTEM]['downloads']
MOVIES = PATHS[SYSTEM]['movies']
SERIES = PATHS[SYSTEM]['series']
DOCKER = PATHS[SYSTEM]['docker']
CONFIG = PATHS[SYSTEM]['docker']


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version=__version__
    )
    subparsers = parser.add_subparsers()

    deploy = subparsers.add_parser('deploy')
    deploy.add_argument('services', nargs='+', choices=SERVICES)
    deploy.add_argument('--downloads-path', type=str, default=DOWNLOADS)
    deploy.add_argument('--movies-path', type=str, default=MOVIES)
    deploy.add_argument('--series-path', type=str, default=SERIES)
    deploy.add_argument('--docker-path', type=str, default=DOCKER)
    deploy.add_argument('--config-path', type=str, default=CONFIG)

    args = parser.parse_args()

    for service in args.services:

        # Get service paths
        service_paths = config.services[service]['paths']

        # Create directories
        create_directories(service_paths)

        # Get docker path
        docker_path = os.path.join(
            config.paths[SYSTEM]['docker'], service, f'{service}-compose.yml'
        )

        # Copy .yml files
        copy_docker_yml(service, docker_path)

        # Run docker
        validate_docker_installation()
        run_docker_yml(service, docker_path)


def validate_docker_installation():
    try:
        subprocess.call('docker version')
    except Exception:
        print('Please install Docker CLI')
        quit()


def create_directories(paths):

    for path in paths.values():
        if not os.path.exists(path):
            os.makedirs(path)


def copy_docker_yml(service, dst):

    src = f'./docker/{service}-compose.yml'

    with open(src, 'r') as source, open(dst, 'w+') as destination:
        template = Template(source.read())
        render = template.render(config.services[service]['paths'])
        destination.write(render)


def run_docker_yml(service, path):

    cmd = f'docker-compose -f {path} up -d'
    subprocess.call(cmd)


if __name__ == '__main__':
    main()
