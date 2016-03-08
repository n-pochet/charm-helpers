# Copyright 2016 Canonical Limited.
#
# This file is part of charm-helpers.
#
# charm-helpers is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3 as
# published by the Free Software Foundation.
#
# charm-helpers is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with charm-helpers.  If not, see <http://www.gnu.org/licenses/>.
from charmhelpers.contrib.hardening.audits.file import TemplatedFile
from charmhelpers.contrib.hardening.host import TEMPLATES_DIR
from charmhelpers.contrib.hardening import utils


def get_audits():
    """Returns the audits used to verify the login.defs file"""
    audits = [TemplatedFile('/etc/login.defs', LoginContext(),
                            template_dir=TEMPLATES_DIR,
                            user='root', group='root', mode=0o0444)]
    return audits


class LoginContext(object):

    def __call__(self):
        settings = utils.get_settings('os')
        ctxt = {
            'additional_user_paths':
            settings['environment']['extra_user_paths'],
            'umask': settings['environment']['umask'],
            'pwd_max_age': settings['auth']['pw_max_age'],
            'pwd_min_age': settings['auth']['pw_min_age'],
            'uid_min': settings['auth']['uid_min'],
            'sys_uid_min': settings['auth']['sys_uid_min'],
            'sys_uid_max': settings['auth']['sys_uid_max'],
            'gid_min': settings['auth']['gid_min'],
            'sys_gid_min': settings['auth']['sys_gid_min'],
            'sys_gid_max': settings['auth']['sys_gid_max'],
            'login_retries': settings['auth']['retries'],
            'login_timeout': settings['auth']['timeout'],
            'chfn_restrict': settings['auth']['chfn_restrict'],
            'allow_login_without_home': settings['auth']['allow_homeless']
        }

        return ctxt
