from fabric.api import env, local, task
from fabric.contrib.project import rsync_project

env.user = 'myles_myles-talks'
env.hosts = ['ssh.phx.nearlyfreespeech.net']


def jekyll(command, *args, **kwargs):
    """Jekyll command line wrapper."""
    opts = []

    for arg in args:
        opts.append('--{0}'.format(arg))

    for key, value in kwargs.items():
        opts.append('--{0}={1}'.format(key, value))

    local('bundle exec jekyll {0} {1}'.format(command, ' '.join(opts)))


@task
def build():
    local('rm -r ./_site/')
    jekyll('build')


@task
def serve():
    jekyll('serve')


@task
def deploy():
    build()

    rsync_project(remote_dir='/home/public/', local_dir='./_site/',
                  delete=True)
