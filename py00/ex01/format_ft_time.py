from datetime import datetime
from time import time

try:
    now = time()

    print(f'Seconds since January 1, 1970: {now:,.4f} or {now:.2e} in '
          f'scientific notation')
    print(datetime.now().strftime("%b %d %Y"))
except Exception as e:
    print(f"Error: {e}")
