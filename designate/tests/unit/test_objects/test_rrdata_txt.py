# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from oslo_log import log as logging
import oslotest.base
import testtools

from designate import exceptions

from designate import objects

LOG = logging.getLogger(__name__)


class RRDataTXTTest(oslotest.base.BaseTestCase):

    def test_reject_non_quoted_spaces(self):
        record = objects.TXT(data='foo bar')
        with testtools.ExpectedException(exceptions.InvalidObject):
            record.validate()

    def test_reject_non_escaped_quotes(self):
        record = objects.TXT(data='foo"bar')
        with testtools.ExpectedException(exceptions.InvalidObject):
            record.validate()