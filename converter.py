import json
from tqdm import tqdm

output = {
    "classes": ["DATE", "EN_SONG", "EN_ARTIST", "EN_GROUP", "KR_SONG", "KR_ARTIST", "KR_GROUP"],
    "annotations" : []
}

with open("dev.jsonl", 'r') as jsonfile:
    jsonlist = list(jsonfile)

for json_str in jsonlist:
    result = json.loads(json_str)
    annos = []
    text = result['text']
    annos.append(text)

    entities = {
        "entities": result['label']
    }
    annos.append(entities)

    output['annotations'].append(annos)
    # print(annos)

with open("devNew.json", "w") as outfile:
    json.dump(output, outfile, ensure_ascii=False)
