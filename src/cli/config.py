import os
import platform

system = platform.system()

paths = {
    'Windows': {
        'downloads': os.path.expanduser('~/Downloads'),
        'movies': os.path.expanduser('~/Videos/Movies'),
        'series': os.path.expanduser('~/Videos/Series'),
        'config': os.path.expanduser('~/.linuxserver'),
        'docker': os.path.expanduser('~/.linuxserver/docker'),
    },
    'Linux': {
        'downloads': os.path.expanduser('~/Downloads'),
        'movies': os.path.expanduser('~/Videos/Movies'),
        'series': os.path.expanduser('~/Videos/Series'),
        'config': os.path.expanduser('~/.linuxserver'),
        'docker': os.path.expanduser('~/.linuxserver/docker'),
    },
    'Darwin': {
        'downloads': os.path.expanduser('~/Downloads'),
        'movies': os.path.expanduser('~/Movies/Movies'),
        'series': os.path.expanduser('~/Movies/Series'),
        'config': os.path.expanduser('~/.linuxserver'),
        'docker': os.path.expanduser('~/.linuxserver/docker'),
    },
}

services = {
    'deluge': {
        'paths': {
            'downloads': paths[system]['downloads'],
            'docker': os.path.join(paths[system]['docker'], 'deluge'),
            'config': os.path.join(paths[system]['config'], 'deluge'),
        },
    },
    'gluetun': {
        'paths': {
            'docker': os.path.join(paths[system]['docker'], 'gluetun'),
            'config': os.path.join(paths[system]['config'], 'gluetun'),
        }
    },
    'jackett': {
        'paths': {
            'downloads': paths[system]['downloads'],
            'docker': os.path.join(paths[system]['docker'], 'jackett'),
            'config': os.path.join(paths[system]['config'], 'jackett'),
        },
    },
    'plex': {
        'paths': {
            'downloads': paths[system]['downloads'],
            'movies': paths[system]['movies'],
            'series': paths[system]['series'],
            'docker': os.path.join(paths[system]['docker'], 'plex'),
            'config': os.path.join(paths[system]['config'], 'plex'),
        },
    },
    'radarr': {
        'paths': {
            'downloads': paths[system]['downloads'],
            'movies': paths[system]['movies'],
            'docker': os.path.join(paths[system]['docker'], 'radarr'),
            'radarr': os.path.join(paths[system]['config'], 'radarr'),
            'config': os.path.join(paths[system]['config'], 'radarr'),
        },
    },
    'sonarr': {
        'paths': {
            'downloads': paths[system]['downloads'],
            'series': paths[system]['series'],
            'docker': os.path.join(paths[system]['docker'], 'sonarr'),
            'config': os.path.join(paths[system]['config'], 'sonarr'),
        },
    },
    'heimdall': {
        'paths': {
            'docker': os.path.join(paths[system]['docker'], 'heimdall'),
            'config': os.path.join(paths[system]['config'], 'heimdall'),
        },
    },
}
