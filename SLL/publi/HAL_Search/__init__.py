import requests
import json
import numpy as np
import re

def json_HAL(authors):
    hal_articles = []
    if authors != ['']:
        for author in authors:
            uri = f'https://api.archives-ouvertes.fr/search/?q={author}&wt=json'
            try:
                request_data = requests.get(uri)
                data = request_data.json()
                for doc in data['response']['docs']:
                    data_tab = []
                    if 'docid' in doc:
                        docid = np.array([doc['docid']])
                    if 'label_s' in doc:
                        label_s=(doc['label_s'])
                        label_s_modif = re.sub(r"&#.*",'',  label_s, flags=re.IGNORECASE )
                        label_s = np.array([label_s_modif])
                    if 'uri_s' in doc:
                        uri_s = np.array([doc['uri_s']])

                    data_tab.append(docid)
                    data_tab.append(label_s)
                    data_tab.append(uri_s)
                    tab = np.array([data_tab])
                    hal_articles.append(tab)
            except json.JSONDecodeError as e:
                    print("Invalid Json syntax", e)
        else:
            pass
    return hal_articles
