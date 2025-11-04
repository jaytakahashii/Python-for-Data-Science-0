from datetime import datetime
import time

print('-- - Using time module ---')
timestamp = time.time()
print(
    f"Seconds since January 1, 1970: {timestamp:,.4f}"
    f" or {timestamp:.2e} in scientific notation"
)
print(time.strftime("%b %d %Y", time.localtime(timestamp)))

print('\n-- - Using datetime module ---')
now = datetime.now()
timestamp = now.timestamp()
print(
    f"Seconds since January 1, 1970: {timestamp:,.4f}"
    f" or {timestamp:.2e} in scientific notation"
)
print(now.strftime("%b %d %Y"))
