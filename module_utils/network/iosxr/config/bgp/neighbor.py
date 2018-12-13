# This code is part of Ansible, but is an independent component.
# This particular file snippet, and this file snippet only, is BSD licensed.
# Modules you write using this snippet, which is embedded dynamically by Ansible
# still belong to the author of the module, and may assign their own license
# to the complete work.
#
# (c) 2016 Red Hat Inc.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
# USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
from ansible.module_utils.network.common.utils import to_list
from ansible.module_utils.network.iosxr.config import ConfigBase
from ansible.module_utils.network.iosxr.config.bgp import get_bgp_as
from ansible.module_utils.network.iosxr.config.bgp.timer import BgpTimer


class BgpNeighbor(ConfigBase):

    argument_spec = {
        'neighbor': dict(required=True),
        'remote_as': dict(type='int', required=True),
        'update_source': dict(),
        'password': dict(no_log=True),
        'enabled': dict(type='bool'),
        'description': dict(),
        'ebgp_multihop': dict(type='int'),
        'tcp_mss': dict(type='int'),
        'timers': dict(type='dict', elements='dict', options=BgpTimer.argument_spec),
        'use_neighbor_group': dict(),
        'state': dict(choices=['present', 'absent'], default='present')
    }

    identifier = ('neighbor', )

    def render(self, config=None):
        commands = list()

        if self.state == 'absent':
            cmd = 'neighbor %s' % self.neighbor
            if not config or cmd in config:
                commands = ['no %s' % cmd]

        elif self.state in ('present', None):
            context = 'neighbor %s' % self.neighbor
            section = ['router bgp %s' % get_bgp_as(config), context]
            config = self.get_section(config, section)
            cmd = 'remote-as %s' % (self.remote_as)
            if not config or cmd not in config:
                commands.append(' '.join([context, cmd]))
            for attr in self.argument_spec:
                if attr in self.values:
                    meth = getattr(self, '_set_%s' % attr, None)
                    if meth:
                        command = meth(config)
                        if command:
                            commands.extend(to_list(' '.join([context,
                                                              command])))
        return commands

    def _set_description(self, config=None):
        cmd = 'description %s' % self.description
        if not config or cmd not in config:
            return cmd

    def _set_enabled(self, config=None):
        cmd = 'shutdown'
        if self.enabled is True:
            cmd = 'no %s' % cmd
        if not config or cmd not in config:
            return cmd

    def _set_update_source(self, config=None):
        cmd = 'update-source %s' % (self.update_source.replace(' ', ''))
        if not config or cmd not in config:
            return cmd

    def _set_password(self, config=None):
        cmd = 'password %s' % self.password
        if not config or cmd not in config:
            return cmd

    def _set_ebgp_multihop(self, config=None):
        cmd = 'ebgp-multihop %s' % self.ebgp_multihop
        if not config or cmd not in config:
            return cmd

    def _set_tcp_mss(self, config=None):
        cmd = 'tcp mss %s' % self.tcp_mss
        if not config or cmd not in config:
            return cmd

    def _set_advertisement_interval(self, config=None):
        cmd = 'advertisement-interval %s' % self.advertisement_interval
        if not config or cmd not in config:
            return cmd

    def _set_neighbor_group(self, config=None):
        cmd = 'use neighbor-group %s' % self.neighbor_group
        if not config or cmd not in config:
            return cmd

    def _set_timers(self, config):
        """generate bgp timer related configuration
        """
        timer = BgpTimer(**self.timers)
        resp = timer.render(config)
        if resp:
            return resp
