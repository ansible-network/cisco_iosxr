# Save active configuration to config.boot
The `config_manager/save` function will save the current active configuration to
disk0:_tmp_config_ansible. This function is idempotent.

## How to save the active configuration
To save the current active configuration to disk0:_tmp_config_ansibl simply
invoke the `config_manager/save` function on the target device. There are no
additional configuration options available for this function.

Below is an example of calling the `config_manager/save` function from the playbook.

```
- hosts: iosxr

  roles:
    - name: ansible-network.cisco_iosxr
      function: config_manager/save
```

## Arguments

None

## Notes
None
