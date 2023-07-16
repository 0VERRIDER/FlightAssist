import sys

sys.path.append('/core/')
sys.path.append('/test/')

import tests.unittests as unittests

if __name__ == '__main__':
    unittests.run_tests()