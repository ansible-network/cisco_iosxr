# cisco_iosxr

This Ansible Network role provides a set of platform dependent fuctions that
are designed to work with Cisco IOS-XR network devices.  The functions included
int his role inlcuding both configuration and fact collection.

## Requirements

* Ansible 2.6 or later
* Ansible Network Engine Role 2.6.0 or later

## Functions

This section provides a list of the availabe functions that are including
in this role.  Any of the provided functions can be implemented in Ansible
playbooks to perform automation activities on Cisco iosxr devices.

Please see the documentation link for each function for details on how to use
the function in an Ansible playbook.

* get_facts [[source]](https://github.com/ansible-network/cisco_iosxr/blob/devel/tasks/get_facts.yaml) [[docs]](https://github.com/ansible-network/cisco_iosxr/blob/devel/docs/get_facts.md)
* configure_vlans [[source]](https://github.com/ansible-network/cisco_iosxr/blob/devel/tasks/configure_vlans.yaml) [[docs]](https://github.com/ansible-network/cisco_iosxr/blob/devel/docs/configure_vlans.md)
* configure_system_properties [[source]](https://github.com/ansible-network/cisco_iosxr/blob/devel/tasks/configure_system_properties.yaml) [[docs]](https://github.com/ansible-network/cisco_iosxr/blob/devel/docs/configure_system_properties.md)

### Config Manager

* config_manager/get [[source]](https://github.com/ansible-network/cisco_iosxr/blob/devel/tasks/config_manager/get.yaml) [[docs]](https://github.com/ansible-network/cisco_iosxr/blob/devel/docs/config_manager/get.md)
* config_manager/save [[source]](https://github.com/ansible-network/cisco_iosxr/blob/devel/tasks/config_manager/save.yaml) [[docs]](https://github.com/ansible-network/cisco_iosxr/blob/devel/docs/config_manager/save.md)
* config_manager/load [[source]](https://github.com/ansible-network/cisco_iosxr/blob/devel/tasks/config_manager/load.yaml) [[docs]](https://github.com/ansible-network/cisco_iosxr/blob/devel/docs/config_manager/load.md)

## License

GPLv3

## Author Information

Ansible Network Community
