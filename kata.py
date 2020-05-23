def sum_of_intervals(intervals):
    list_to_be_summed = []
    for interval in intervals:
        for i in intervals:
            i = list(i)
            if "done" in i:
                pass
            elif i[0] > interval[0] and i[1] < interval[1]:
                pass
            elif i[0] < interval[0] and i[1] < interval[1]:
                list_to_be_summed.append(i[0] - interval[0])
            elif i[0] > interval[0] and i[1] > interval[1]:
                list_to_be_summed.append(interval[1] - i[1])
            elif i[0] < interval[0] and i[1] > interval[1]:
                list_to_be_summed.append(i[0] - interval[0] + interval[1] - i[1])
            else:
                list_to_be_summed.append(interval[1] - interval[0])
            i.append('done')
    return sum(list_to_be_summed)
