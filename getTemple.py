import requests
import re


def getT():
    url = "https://th.wikipedia.org/wiki/รายชื่อวัดในจังหวัดพะเยา"
    response = requests.get(url)
    html_content = response.text

    li_match = re.findall('>(.*?)<', html_content)
    li_match = [e for e in li_match if re.match('^วัด', e)]
    li_match = [e for e in li_match if re.match('(?!วัดราษฏร์ใน)', e)]
    li_match = [e for e in li_match if re.match('(?!วัดราษฏร์มหา)', e)]
    li_match = [e for e in li_match if re.match('(?!วัดราษฏร์ธรรม)', e)]

    li_match = [re.sub('\([^)]*\)', '', e) for e in li_match]

    li_match = li_match[:-4]
    li_match = list(set(li_match))
    return li_match
