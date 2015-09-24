# This python program is to read record from log file.
import sys
import xml.etree.ElementTree as ET

welcome_info="File Reader {version_id} \tLast Updated: {date} \tCopyright: Jianguo HAO @UQAC"
version="0.0.1"
update_date="23/09/2015"
help_infomation="Help!!!"

print(welcome_info.format(version_id=version, date=update_date))
print("Type \"help\""+"for more information.")

screen_type = raw_input(">>>")

if screen_type=="help":
    print(help_infomation)
else:
    print("Please type the file name:")
