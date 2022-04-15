from tours import data


def general_info(request):
    return {"departures": data.departures, "gen_info": data.gen_info}
