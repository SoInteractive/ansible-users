from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_directories(host):
    present = [
        "/root/.ssh"
    ]
    if present:
        for directory in present:
            d = host.file(directory)
            assert d.is_directory
            assert d.exists


def test_files(host):
    present = [
        "/opt/slack.sh",
        "/root/.ssh/authorized_keys",
        "/etc/pam.d/sshd"
    ]
    if present:
        for file in present:
            f = host.file(file)
            assert f.exists
            assert f.is_file
