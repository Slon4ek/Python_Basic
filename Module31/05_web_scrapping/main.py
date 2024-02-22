import re
import requests

my_req = requests.get('http://www.columbia.edu/~fdc/sample.html')
if my_req.status_code == 200:
    print(re.findall(r'<h3 .*>(.*)</h3>', my_req.text))

# В данном случае запрос request.get заменен на загрузку сайта из файла html
with open('examples.html', 'r') as f:
    text = f.read()
    print(re.findall(r'<h3>(.*)</h3>', text))
# По итогу вы так же получаете код сайта в виде одной строки
