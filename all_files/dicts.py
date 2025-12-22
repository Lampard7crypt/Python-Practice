# ========================================================================================
# Learn more about Python Sort and sorted functions!
def sort_by_age(s: list):
    return sorted(s, key=lambda item: item[1])

# print(sort_by_age([('Alice', 30), ('Bob', 25), ('Eve', 35)]))

def count_vowels(s: str) -> str:
    return len([letter for letter in s if letter in ['a', 'e', 'i', 'o', 'u']])

# print(count_vowels("vowel"))



def converter(amount):
    currencies = ["EUR", "CAD", "GBP", "USD", "KSH"]
    amount = int(input("Enter amount you want to convert: "))
    while True:
        currency = input("Source currency: ")
        if currency not in currencies:
            print('Not valid currency, try "EUR", "CAD", "GBP", "USD" or "KSH"')
        else:
            break
    
    if currency == "USD":
        return {"EUR": amount*0.9, "CAD": amount*1.1, "GBP": amount*0.85, "KSH": amount/0.013}
    if currency == "CAD":
        return {"EUR": amount*0.9, "USD": amount/1.1, "GBP": amount*0.85, "KSH": amount*0.013}
    if currency == "GBP":
        return {"EUR": amount*0.9, "CAD": amount*1.1, "USD": amount/0.85, "KSH": amount*0.013}
    if currency == "KSH":
        return {"EUR": amount*0.9, "CAD": amount*1.1, "GBP": amount*0.85, "USD": amount*0.013}

# print(converter(amount))

