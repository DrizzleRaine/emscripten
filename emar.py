#!/usr/bin/env python3
# Copyright 2016 The Emscripten Authors.  All rights reserved.
# Emscripten is available under two separate licenses, the MIT license and the
# University of Illinois/NCSA Open Source License.  Both these licenses can be
# found in the LICENSE file.

"""Archive helper script

This script acts as a frontend replacement for `llvm-ar`.
"""

import sys

from tools import shared, building


#
# Main run() function
#
def run():
  return shared.run_process([shared.LLVM_AR] + building.get_command_with_possible_response_file(sys.argv[1:]), stdin=sys.stdin, check=False).returncode


if __name__ == '__main__':
  sys.exit(run())
