def YMDE(datee):
    data = dict()
    date, data['expire'] = datee.split()
    data['year'], data['month'], data['date'] = map(int, date.split("."))
    return(data)

def solution(today, terms, privacies):
    answer = []
    terms_data = dict()
    for i in terms:
        n, m = i.split()
        terms_data[n] = int(m)
    today_year, today_month, today_date = map(int, today.split("."))
    for idx, i in enumerate(privacies):
        data = YMDE(i)
        calc_month = data['month'] + terms_data[data['expire']] % 12
        calc_year = data['year'] + terms_data[data['expire']] // 12
        if calc_month > 12:
            calc_year = calc_year + calc_month//12
            calc_month = calc_month % 12
            if calc_month == 0:
                calc_month = 12
                
        #print(calc_year, calc_month, data['date'])
        if today_year > calc_year:
            print(1)
            answer.append(idx+1)
        elif today_year == calc_year:
            if today_month > calc_month:
                print(2)
                answer.append(idx+1)
            elif today_month == calc_month:
                if today_date >= data['date']:
                    print(3)
                    answer.append(idx+1)
                else:
                    print(4)
                    continue
            else:
                print(5)
                continue
        else:
            print(6)
            continue

    return answer