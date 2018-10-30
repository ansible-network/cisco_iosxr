===========================
Ansible Network cisco_iosxr
===========================

.. _Ansible Network cisco_iosxr_v2.7.0:

v2.7.0
======

.. _Ansible Network cisco_iosxr_v2.7.0_New Tasks:

New Tasks
---------

- Add ``configure_user`` task.


.. _Ansible Network cisco_iosxr_v2.6.0:

v2.6.0
======

.. _Ansible Network cisco_iosxr_v2.6.0_Major Changes:

Major Changes
-------------

- Initial release of the ``cisco_iosxr`` Ansible role.

- This role provides functions to perform automation activities on Cisco IOSXR devices.


.. _Ansible Network cisco_iosxr_v2.6.0_New Functions:

New Functions
-------------

- NEW ``get_facts`` function can be used to collect facts from Cisco IOSXR devices.

- NEW ``config_manager/get`` function returns the either the current active or current saved configuration from Cisco IOSXR devices.

- NEW ``config_manager/load`` function provides a means to load a configuration file onto a target device running Cisco IOSXR.

- NEW ``config_manager/save`` function saves the current active (running) configuration to the startup configuration.

