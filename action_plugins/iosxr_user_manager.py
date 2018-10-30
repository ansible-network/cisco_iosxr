# (c) 2018, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'network'}

from ansible.plugins.action import ActionBase

class UserManager:

    def __init__(self, new_users, user_config_data):
        self.__new_users = new_users
        self.__user_config_data = user_config_data

    def generate_existing_users(self):
        users = self.__user_config_data.strip().rstrip('!').split('!')

        if not users:
            return []

        existing_users = []

        for user in users:
            user_config = user.strip().splitlines()

            name = user_config[0].strip().split()[1]
            group = None

            if len(user_config) > 1:
                group_or_secret = user_config[1].strip().split()
                if group_or_secret[0] == 'group':
                    group = group_or_secret[1]

            obj = {
                'name': name,
                'group': group
            }

            existing_users.append(obj)

        return existing_users

    def filter_users(self):
        want = self.__new_users
        have = self.generate_existing_users()
        filtered_users = [x for x in want if x not in have]

        changed = True if len(filtered_users) > 0 else False

        return changed, filtered_users


class ActionModule(ActionBase):

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()

        result = super(ActionModule, self).run(tmp, task_vars)

        try:
            new_users = self._task.args['new_users']
            user_config_data = self._task.args['user_config']
        except KeyError as exc:
            return {'failed': True, 'msg': 'missing required argument: %s' % exc}

        result['changed'], result['stdout'] = UserManager(new_users, user_config_data).filter_users()

        return result
