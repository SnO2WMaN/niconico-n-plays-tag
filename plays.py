import requests

for n in range(1, 1000):
    tag = str(n) + "再生"
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
