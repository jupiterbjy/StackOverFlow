from urllib.request import urlopen

page = urlopen("http://woodburytheatre.com/showtimes")
html_bytes = page.read()
html = html_bytes.decode("utf-8")

span_index = html.find("<div id=\"showtimes_wrapper\">")
start_index = span_index + len("<div id=\"showtimes_wrapper\">")
end_index = html.find("<div id=\"t_comingsoon\">")

movie_info = html[start_index:end_index]

# this line below
movie_list = [i.split('/')[-1].rstrip(r"'>") for i in movie_info.split("\n") if 'showtimes_movie' in i]
print(movie_list)
