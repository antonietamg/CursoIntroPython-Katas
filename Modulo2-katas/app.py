import pipdate
if pipdate.needs_checking("dateutil"):
    print(pipdate.check("dateutil", "2.8.2"))

from datetime import *
from dateutil.relativedelta import *
import dateutil
now = datetime.now()
print(now)

now = now + relativedelta(months=5, weeks=0, hour=2)

print(now)




