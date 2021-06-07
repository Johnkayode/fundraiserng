from datetime import datetime, date


def find_date_difference(date_str):
    today = date.today()

    try:
        mydate = datetime.strptime(date_str, "%d-%m-%Y").date()
    except:
        mydate = datetime.strptime(date_str, "%d/%m/%Y").date()

    return (mydate - today).days


