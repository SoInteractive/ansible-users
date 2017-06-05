from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_directories(File):
    present = [
        "/root/.ssh"
    ]
    if present:
        for directory in present:
            d = File(directory)
            assert d.is_directory
            assert d.exists


def test_files(File):
    present = [
        "/opt/slack.sh",
        "/root/.ssh/authorized_keys",
        "/etc/pam.d/sshd"
    ]
    if present:
        for file in present:
            f = File(file)
            assert f.exists
            assert f.is_file
