import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_sudoers_file(host): 
    with host.sudo():
        f = host.file('/etc/sudoers.d/ro1423')
        assert f.exists
        assert f.contains('ro1423')
  
    
