import requests

for n in list(range(1, 10)) + [2000, 10000]:
    tag = str(n) + "万再生"
    res = requests.get(
        "https://api.search.nicovideo.jp/api/v2/snapshot/video/contents/search",
        params={
            "q": "",
            "targets": "tags",
            "filters[tagsExact][0]": tag,
            "_sort": "-viewCounter",
        },
    )
    count = res.json()["meta"]["totalCount"]
    if count == 0:
        continue
    print(count, tag)
