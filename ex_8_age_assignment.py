def age_assignment(*args, **kwargs):
    result = dict()

    for name in args:
        first_letter = name[0]
        if first_letter in kwargs:
            age = kwargs[first_letter]
            result[name] = age
    name_book =[f"{name} is {age} years old." for name, age in  sorted(result.items())]
    return '\n'.join(name_book)

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))