from datetime import datetime

start = datetime(2019, 1, 1, 0, 0, 0)
end = datetime.now()


def CreateFunctionTimeSpan(time_unit="m"):
    time_unit_map = {"m": 1, "h": 60, "d": (24 * 60)}

    def f(start, end):
        time_delta = end - start
        return time_delta.total_seconds() / (60 * time_unit_map[time_unit])

    return f


time_span_m = CreateFunctionTimeSpan("m")
print(time_span_m(start, end))

time_span_h = CreateFunctionTimeSpan("h")
print(time_span_h(start, end))

time_span_d = CreateFunctionTimeSpan("d")
print(time_span_d(start, end))
