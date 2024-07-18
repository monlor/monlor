# -*- coding: utf-8 -*
import requests
import xml.etree.ElementTree as ET
import datetime

with open('README.md', 'w') as f:
    f.write(r'''
<h3 align="center">👋 Hello! I'm monlor.</h3>

<p align="center">
  <a href="https://www.monlor.com">Blog</a> •
  <a href="https://github.com/monlor">GitHub</a> •
  <a href="https://linktr.ee/monlor">Linktree</a>
</p>

### Github Statistics

![Stats](https://github-readme-stats.monlor.com/api?username=monlor&show_icons=true&layout=compact&count_private=true&hide_title=true&theme=default&)
![Lang](https://github-readme-stats.monlor.com/api/top-langs/?username=monlor&layout=compact&count_private=true&theme=default&hide=css,html,javascript)

### Latest blog posts

''')
    ret = requests.get('https://www.monlor.com/feed/')
    ret.encoding = 'utf-8'
    feed = ret.text
    root = ET.fromstring(ret.text)
    for item in root.findall('.//item')[:5]:
        text = item.find("title").text
        url = item.find("link").text
        published = item.find("pubDate").text
        time_format = datetime.datetime.strptime(published, '%a, %d %b %Y %H:%M:%S %z')
        f.write('- {} [{}]({})\n'.format(time_format.strftime("%Y-%m-%d"), text, url))

    f.write('''
[>>> More blog posts](https://www.monlor.com/archive.html)
''')
