import random

from django.http import Http404
from django.shortcuts import render

from tours import data


def main_view(request):
    random_tours = dict(random.sample(data.tours.items(), 6))
    return render(request, 'tours/index.html', context={"random_tours": random_tours})


def departure_view(request, departure):
    try:
        start_point = data.departures[departure]
    except KeyError:
        raise Http404

    departure_tours = dict(filter(lambda item: item[1].get("departure") == departure, data.tours.items()))

    prices = [tour['price'] for tour in departure_tours.values()]
    nights = [tour['nights'] for tour in departure_tours.values()]

    min_price = min(prices)
    max_price = max(prices)
    min_nights = min(nights)
    max_nights = max(nights)

    return render(request, 'tours/departure.html', context={
                                                            'departure': start_point,
                                                            "departure_tours": departure_tours,
                                                            "min_price": min_price,
                                                            "max_price": max_price,
                                                            "min_nights": min_nights,
                                                            "max_nights": max_nights,
                                                            })


def tour_view(request, id):
    try:
        tour = data.tours[id]
    except KeyError:
        raise Http404
    return render(request, 'tours/tour.html', context={"tour": tour})


def custom_handler404(request, exception):
    return render(request, 'tours/404.html', status=404)
