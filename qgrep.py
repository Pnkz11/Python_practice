#Code : Copy Qgrep file to LSG


from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import ssl

# This restores the same behavior as before.
context = ssl._create_unverified_context()
QgrepRequest=urlopen("https://qssi.akamai.com/cgi-bin/qgrep_ui/qgrep.pl?screen=results&user=all&num_results_to_view=20", context=context)
QgrepPagehtml=QgrepRequest.read()
QgrepPage=soup(QgrepPagehtml, 'html.parser')
print(QgrepPage.prettify())

##To be continued 



