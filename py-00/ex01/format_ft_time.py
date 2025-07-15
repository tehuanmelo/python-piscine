from datetime import datetime as dt

today = dt.now()
epoch = dt(1970, 1, 1)

seconds_from_epoch = (today - epoch).total_seconds()

print(f"Seconds since January 1, 1970: {seconds_from_epoch:,.4f} or "
      f"{seconds_from_epoch:.2e} in scientific notation")
print(today.strftime('%b %d %Y'))
