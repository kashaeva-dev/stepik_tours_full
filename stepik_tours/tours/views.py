import random

from django.shortcuts import render

from tours import data


def main_view(request):
    random_numbers = []
    while len(random_numbers) != 6:
        random_numbers = list(set([random.randint(1, 16) for i in range(6)]))
    random_tours = dict(filter(lambda item: item[0] in random_numbers, data.tours.items()))
    return render(request, 'tours/index.html', context={"random_tours": random_tours})


def departure_view(request, departure):
    departure_tours = dict(filter(lambda item: item[1].get("departure") == departure, data.tours.items()))
    sorted_price = list(sorted(departure_tours.items(), key=lambda x: x[1].get("price")))
    sorted_nights = list(sorted(departure_tours.items(), key=lambda x: x[1].get("nights")))
    departure = data.departures.get(departure)
    return render(request, 'tours/departure.html', context={'departure': departure, "departure_tours": departure_tours,
                                                            "sorted_price": sorted_price,
                                                            "sorted_nights": sorted_nights})


def tour_view(request, id):
    tour = data.tours.get(id)
    return render(request, 'tours/tour.html', context={"tour": tour})
