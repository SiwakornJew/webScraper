import requests
import re
import csv


def getTem(province):
    url_dict = {
        "prayao": "https://th.wikipedia.org/wiki/รายชื่อวัดในจังหวัดพะเยา",
        "pattani": "https://th.wikipedia.org/wiki/รายชื่อวัดในจังหวัดปัตตานี",
        "Ayutthaya": "https://th.wikipedia.org/wiki/รายชื่อวัดในจังหวัดพระนครศรีอยุธยา",
        "PrachinBuri": "https://th.wikipedia.org/wiki/รายชื่อวัดในจังหวัดปราจีนบุรี"
    }
    if province not in url_dict:
        return None
    url = url_dict[province]
    match province:
        case "prayao":
            response = requests.get(url)
            html_content = response.text
            li_match = re.findall('>(.*?)<', html_content)
            li_match = [e for e in li_match if re.match('^วัด', e)]
            li_match = [e for e in li_match if re.match('(?!วัดราษฏร์ใน)', e)]
            li_match = [e for e in li_match if re.match('(?!วัดราษฏร์มหา)', e)]
            li_match = [e for e in li_match if re.match(
                '(?!วัดราษฏร์ธรรม)', e)]

            li_match = [re.sub('\([^)]*\)', '', e) for e in li_match]

            li_match = li_match[:-4]
            li_match = list(set(li_match))
            return li_match

        case "pattani":
            response = requests.get(url).text
            li = re.findall('>(.*?)<', response)
            li = [i for i in li if re.match('^วัด', i)]
            li = [i for i in li if re.match('(?!วัดราษฏร์)', i)]
            for i in range(len(li)):
                li[i] = re.sub(r'\s*\([^)]*\)\s*$', '', li[i])
            result = li[:-4]
            return result

        case "Ayutthaya":
            response = requests.get(url)
            html_content = response.text

            li_match = re.findall('>(.*?)<', html_content)
            li_match = [e for e in li_match if re.match('^วัด', e)]
            li_match = [e for e in li_match if re.match('(?!วัดราษฏร์ใน)', e)]
            li_match = [e for e in li_match if re.match('(?!วัดราษฎร์ใน)', e)]
            li_match = [e for e in li_match if re.match('(?!วัดราษฏร์มหา)', e)]
            li_match = [e for e in li_match if re.match('(?!วัดราษฎร์มหา)', e)]

            li_match = [e for e in li_match if re.match('(?!วัดใน)', e)]
            li_match = [e for e in li_match if re.match('(?!วัดหลวงใน)', e)]
            li_match = [e for e in li_match if re.match('(?!วัดไทย)', e)]
            li_match = [e for e in li_match if re.match(
                '(?!วัดหน้าพระเมรุ)', e)]
            li_match = [e for e in li_match if re.match(
                '(?!วัดราษฎร์ธรรม)', e)]

            li_match = [re.sub('\([^)]*\)', '', e) for e in li_match]
            li_match = [re.sub('ตำบล.*?', '', e) for e in li_match]
            li_match = [re.sub(' หรือ', '', e) for e in li_match]

            li_match = list(set(li_match))
            li_match.sort()
            li_match = li_match[1:]

            return li_match

        case "PrachinBuri":
            response = requests.get(url)
            html_content = response.text

            li_match = re.findall('>(.*?)<', html_content)
            li_match = [e for e in li_match if re.match('^วัด', e)]
            li_match = [e for e in li_match if re.match('(?!วัดราษฏร์ใน)', e)]
            li_match = [e for e in li_match if re.match('(?!วัดราษฏร์มหา)', e)]
            li_match = [e for e in li_match if re.match('(?!วัดหลวงใน)', e)]
            li_match = [e for e in li_match if re.match(
                '(?!วัดราษฎร์ธรรม)', e)]
            li_match = [re.sub('\([^)]*\)', '', e) for e in li_match]
            li_match = li_match[:-4]
            li_match = list(set(li_match))
            return li_match
