#!/usr/bin/env python

def array_of_names(persons):
    result = []

    for first, last in persons.items():
        full = first.capitalize() + " " + last.capitalize()
        result.append(full)

    return result


#####

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))   