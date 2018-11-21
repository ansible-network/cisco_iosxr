# Configure VLANs on the device

The `configure_vlans` function can be used to set VLANs on Cisco IOS-XR devices.
This function is only supported over `network_cli` connection type and 
requires the `ansible_network_os` value set to `iosxr`.

## How to set VLANs on the device

To set VLANs on the device, simply include this function in the playbook
using either the `roles` directive or the `tasks` directive.  If no other
options are provided, then all of the available facts will be collected for 
the device.

Below is an example of how to use the `roles` directive to set VLANs on the 
Cisco IOS-XR device.

```
- hosts: iosxr

  roles:
  - name ansible-network.cisco_iosxr
    function: configure_vlans
  vars:
    vlans:
      - interface: Gi0/0/0/3
        id: 10
        description: this is vlan 10
        ipaddr: 192.168.1.0/24
```

The above playbook will set the VLANs with ID, description, and address to particular
interface under the `iosxr` top level key.  

### Implement using tasks

The `configure_vlans` function can also be implemented using the `tasks` directive
instead of the `roles` directive.  By using the `tasks` directive, you can
control when the fact collection is run. 

Below is an example of how to use the `configure_vlans` function with `tasks`.

```
- hosts: iosxr

  tasks:
    - name: set vlans to iosxr devices
      import_role:
        name: ansible-network.cisco_iosxr
        tasks_from: configure_vlans
      vars:
        vlans:
          - interface: Gi0/0/0/3
            id: 10
            description: this is vlan 10
            ipaddr: 192.168.1.0/24
```

## Adding new parsers

Over time new parsers can be added (or updated) to the role to add additional
or enhanced functionality.  To add or update parsers perform the following
steps:

* Add (or update) command parser located in `parse_templates/cli`

## Arguments

### interface

VLAN will be configured on the Cisco IOS-XR device using respective interface and hence 
this is a mandatory parameter.

This being a mandatory parameter which means even if the user doesn't pass the respective
argument the role will fail to run with missing argument error.

### id

VLAN will be configured on the Cisco IOS-XR device using respective ID over the interface
and this is also a mandatory parameter.

This being a mandatory parameter which means even if the user doesn't pass the respective
argument the role will fail to run with missing argument error. Also, valid VLANs id
range is 1-4094, so the role checks if the user value for the argument matches the range
and if not the execution of the role fails with id range error

### description

This sets the description for the VLAN Id for the Cisco IOS-XR device.

The default value is `omit` which means even if the user doesn't pass the respective 
value the role will continue to run without any failure.

### ipaddr

This sets the ip address for the VLAN Id for the Cisco IOS-XR device.

The default value is `omit` which means even if the user doesn't pass the respective
value the role will continue to run without any failure.

### state

This sets the VLANs value to the Cisco IOS-XR device and if the value of the state is changed
to `absent`, the role will go ahead and try to delete the VLANs via the arguments passed.

The default value is `present` which means even if the user doesn't pass the respective
argument, the role will go ahead and try to set the VLANs via the arguments passed to the 
Cisco IOS-XR device.

## Notes

None
