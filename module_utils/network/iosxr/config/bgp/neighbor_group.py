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
from ansible.module_utils.network.iosxr.config.bgp import get_bgp_as
from ansible.module_utils.network.iosxr.config.bgp.neighbor import BgpNeighbor


class BgpNeighborGroup(BgpNeighbor):

    argument_spec = {
        'name': dict(required=True)
    }

    argument_spec.update(BgpNeighbor.argument_spec)

    del argument_spec['neighbor']

    identifier = ('name', )

    def render(self, config=None):
        commands = list()

        context = 'neighbor-group %s' % self.name

        if config:
            bgp_as = get_bgp_as(config)
            if bgp_as:
                section = ['router bgp %s' % bgp_as, context]
                config = self.get_section(config, section)

        if self.state == 'absent':
            if context in config:
                commands.append('no %s' % context)

        if self.state == 'present':
            subcommands = list()
            for attr in self.argument_spec:
                if attr in self.values:
                    meth = getattr(self, '_set_%s' % attr, None)
                    if meth:
                        resp = meth(config)
                        if resp:
                            subcommands.extend(to_list(resp))
            if subcommands:
                commands = [context]
                commands.extend(subcommands)
                commands.append('exit')
            elif not config or context not in config:
                commands.extend([context, 'exit'])
        return commands

    def _set_remote_as(self, config=None):
        cmd = 'remote-as %s' % self.remote_as
        if not config or cmd not in config:
            return cmd
