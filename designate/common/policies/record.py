# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


from oslo_policy import policy

from designate.common.policies import base

rules = [
    policy.DocumentedRuleDefault(
        name="find_records",
        check_str=base.RULE_ADMIN_OR_OWNER,
        description='Find records.',
        operations=[
            {
                'path': '/v2/reverse/floatingips/{region}:{floatingip_id}',
                'method': 'GET'
            }, {
                'path': '/v2/reverse/floatingips',
                'method': 'GET'
            }
        ]
    ),
    policy.RuleDefault(
        name="count_records",
        check_str=base.RULE_ADMIN_OR_OWNER)
]


def list_rules():
    return rules
