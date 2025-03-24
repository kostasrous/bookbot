
def word_counter(text):
    data = text.split()
    num_of_words = len(data)
    return num_of_words

def symbol_counter(text):
    text = text.lower()
    symbol_dict={}
    for char in text:
        if char in symbol_dict:
            symbol_dict[char] += 1
        else:
            symbol_dict[char] = 1
    return symbol_dict

def report(dict):
    report_list = []
    for key in dict:
        report_list.append({"name":key,"count":dict[key]})
    report_list.sort(key= lambda x: x["count"] ,reverse= True)




    return report_list