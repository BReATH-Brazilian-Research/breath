import sys
import os

from streamlit import cli as stcli
import breath


if __name__ == '__main__':
    
    
    path = breath.__file__[:-11] + "home.py"

    sys.argv = ["streamlit", "run", path]
    sys.exit(stcli.main())