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
from ansible.module_utils.network.iosxr.config import ConfigBase


class BgpTimer(ConfigBase):

    argument_spec = {
        'keepalive': dict(type='int'),
        'holdtime': dict(type='int'),
        'min_neighbor_holdtime': dict(type='int'),
        'state': dict(choices=['present', 'absent', 'replace'], default='present')
    }

    identifier = ('keepalive', )

    def render(self, config=None):
        cmd = 'timers'

        if self.state in ('present', None):
            if self.keepalive and self.holdtime:
                cmd = '%s %s %s' % (cmd, self.keepalive, self.holdtime)
                if self.min_neighbor_holdtime:
                    cmd += ' %s' % self.min_neighbor_holdtime
                if not config or cmd not in config:
                    return cmd
            else:
                raise ValueError("required both options for timers: keepalive and holdtime")

        elif self.state == 'absent':
            if not config or cmd in config:
                return 'no %s' % cmd
