<p><img src="https://www.iconfinder.com/data/icons/PRACTIKA/256/user.png" alt="user logo" title="user" align="right" height="60" /></p>

Ansible Role: users
===================

[![Build Status](https://ci.devops.sosoftware.pl/buildStatus/icon?job=SoInteractive/users/master)](https://ci.devops.sosoftware.pl/blue/organizations/jenkins/SoInteractive%2Fusers/activity) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/ansible/role/18237.svg)](https://galaxy.ansible.com/SoInteractive/users/) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

Manage users, passwords, and ssh public keys

Overview
--------

Role will copy SSH keys and configure sudo to enable secure passwordless access for user which connects to remote host. It also unauthorizes SSH keys from "insecure_keys" directory. 
Role can reconfigure PAM to enable notifications about failed SSH logins and optionally send slack notifications. 

Disclaimer
----------

Role is created for internal Sointeractive use. However after some tweaking it can be used on other systems.

Role stores public SSH keys for Sointeractive users. This approach isn't treated as a security breach until private keys are stored in secure places.

Example usage
-------------

Use it in a playbook as follows:
```yaml
- hosts: all
  become: true
  roles:
    - SoInteractive.users
```

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.
