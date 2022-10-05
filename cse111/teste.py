from datetime import datetime

today = datetime.now(tz=None)

print(f'{today:%y-%m-%d}')