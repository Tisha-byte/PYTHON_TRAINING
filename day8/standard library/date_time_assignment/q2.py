import datetime
date_string = "Feb 25 2020 4:20PM"

date_object=datetime.datetime.strptime(date_string,'%b %d %Y %I:%M%p')
print(date_object)