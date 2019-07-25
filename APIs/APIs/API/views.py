from django.shortcuts import render
import requests
# Create your views here.

def movies_list(request):
	query = request.GET.get("q")

	url = 'http://www.omdbapi.com/?apikey=714b6f16&s=' +query
	response = requests.get(url)

	context = {
	"movies" : response.json()
	}
	return render(request, "mvlist.html", context)


def movie_details(request, movie_id):
	url = 'http://www.omdbapi.com/?apikey=714b6f16&i=' + movie_id 
	response = requests.get(url)

	context = {
		"movie" : response.json()
	}
	return render(request, 'movie_details.html', context)