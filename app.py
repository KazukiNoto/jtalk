import jtalk
from datetime import datetime

d = datetime.now()
text = '%s月%s日、%s時%s分%s秒' % (d.month, d.day, d.hour, d.minute, d.second)
jtalk.run(text)
