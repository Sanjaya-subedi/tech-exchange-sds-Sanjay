# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

def test_capital(users_input):
  output_dic = {}
  avaiable_capitals = {"New York": "Albany", "California":"Sacramento", "Texas":"Austin", "Montana":"Helena", "Ohio":"Columbus"}
  for state, capital in users_input.items():
    if capital == avaiable_capitals[state]:
      if not "Correct" in output_dic:
        output_dic["Correct"] = [state]
      else:
        output_dic["Correct"] += [state]
    else:
      if not "Incorrect" in output_dic:
        output_dic["Incorrect"] = [state]
      else:
        output_dic["Incorrect"] += [state]
  return output_dic


