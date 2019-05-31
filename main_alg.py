input = input("what is the order type?")

if input = "hoodie":
    input = hoodie
elif input = "tshirt"
    input = tshirt

items = { hoodie : 6, tshirt : 3}

supplies = {hoodie : "list of supplies for hoodie", tshirt : "list of supplies for tshirt"}

month_t = [[[6],[6],[6],[6],[6],[6],[6]],
           [[6],[6],[6],[6],[6],[6],[6]],
           [[6],[6],[6],[6],[6],[6],[6]],
           [[6],[6],[6],[6],[6],[6],[6]]]

month_o = [[[],[],[],[],[],[],[]],
           [[],[],[],[],[],[],[]],
           [[],[],[],[],[],[],[]],
           [[],[],[],[],[],[],[]]]

def add_order(order):
    idx = 0
    idy = 0
    work = items[order]

    while work > 0:
        for week in month:
            for day in week:
                if month_t[idy][idx] > 0:
                    if work <= month_t[idy][idx]:
                        month_t[idy][idx] -= work
                        month_o[idy][idx] = holder
                        holder.append((order, (str(work),"segments"), supplies[order]))

                    elif work > month_t[idy][idx]:
                        segs = str(month_t[idy][idx] - work)*(-1))
                        work -= month_t[idy][idx]
                        month_o[idy][idx] = holder
                        holder.append((order, (segs,"segments"), supplies[order]))
            idx += 1
        idy += 1

add_order(order)
