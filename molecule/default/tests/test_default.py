import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_apt_repo(host):
    test_pkg = host.package("ansible-apt-test-en")
    assert test_pkg.is_installed


def test_proxy_config(host):
    apt_proxy_conf = host.file("/etc/apt/apt.conf.d/01proxy")
    assert apt_proxy_conf.is_file
    assert apt_proxy_conf.contains("Ansible managed")
