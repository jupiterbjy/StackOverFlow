from urllib.parse import urlparse

url_list = ["https://www.ox.ac.uk/",
            "http://www.ox.ac.uk/",
            "https://www.ox.ac.uk",
            "http://www.ox.ac.uk",
            "https://www.ox.ac.uk/index.php",
            "https://www.ox.ac.uk/index.html",
            "http://www.ox.ac.uk/index.php",
            "http://www.ox.ac.uk/index.html",
            "www.ox.ac.uk/",
            "ox.ac.uk",
            "ox.ac.uk/research",
            "ox.ac.uk/index.php?12"
            ]

def url_stripper(source: list):
    replace_dict = {"http://": "", "https://": ""}

    for url in source:
        # Unify scheme to HTTP
        for key, val in replace_dict.items():
            url = url.replace(key, val, 1)

        url = "http://" + (url[4:] if url.startswith("www.") else url)
        parsed = urlparse(url)



print(set(url_stripper(url_list)))
