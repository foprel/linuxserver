from jinja2 import Template
from version import __version__
from . import config
import argparse
import os
import subprocess


SYSTEM = config.system
SERVICES = config.services.keys()
PATHS = config.paths
ROOT = os.path.dirname(__file__)


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
        copy_docker_yml(service, ROOT, docker_path)

        # Run docker
        validate_docker_installation()
        run_docker_yml(service, docker_path)


def validate_docker_installation():
    try:
        subprocess.call('docker version', shell=True)
    except Exception:
        print('Please install Docker CLI')
        quit()


def create_directories(paths):

    for path in paths.values():
        if not os.path.exists(path):
            os.makedirs(path)


def copy_docker_yml(service, src, dst):

    src = f'{src}/docker/{service}-compose.yml'

    with open(src, 'r') as source, open(dst, 'w+') as destination:
        template = Template(source.read())
        render = template.render(config.services[service]['paths'])
        destination.write(render)


def run_docker_yml(service, dst):

    vars = (
        f'OPENVPN_USER={os.environ.get("OPENVPN_USER")} '
        f'WIREGUARD_PRIVATE_KEY={os.environ.get("WIREGUARD_PRIVATE_KEY")} '
        f'WIREGUARD_ADDRESSES={os.environ.get("WIREGUARD_ADDRESSES")} '
    )

    cmps = (
        f'docker compose -f {dst} up -d'
    )

    if service == 'gluetun':
        cmds = vars + cmps
    else:
        cmds = cmps
        
    print(cmds)
    subprocess.call(cmds, shell=True)


if __name__ == '__main__':
    main()
