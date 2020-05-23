import datetime as dt


class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_data(self):
        if len(self.title) == 0:
            raise Exception("Title is empty!")
        if self.start > self.end:
            raise ValueError("Start date is later than end date!")

    @classmethod
    def publish_offer(cls, list_of_trips):
        list_of_errors = []
        for trip in list_of_trips:
            try:
                trip.check_data()
            except ValueError as e:
                list_of_errors.append(f"{trip.symbol}, {str(e)}")
            except Exception as e:
                list_of_errors.append(f"{trip.symbol}, {str(e)}")
        if list_of_errors:
            raise Exception(f"The list of trips has errors: {list_of_errors}")
        print("the offer will be published...")


trips = [
    Trip("IT-VNC", "Italy-Venice", dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
    Trip("SP-BRC", "Spain-Barcelona", dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
    Trip("IT-ROM", "Italy-Rome", dt.date(2023, 6, 21), dt.date(2023, 6, 12)),
]

try:
    print("Publishing trips...")
    Trip.publish_offer(trips)
    print("... done")
except Exception as e:
    print("Critical:")
    print(e)
