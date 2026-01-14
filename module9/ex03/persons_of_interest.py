#!/usr/bin/env python

def value_getter(item):
    return item[1]["date_of_birth"]

def famous_births(women_scientists):
    return dict(sorted(women_scientists.items(), key=value_getter))


women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
sorted_science = famous_births(women_scientists)

for person in sorted_science.items():
    print(person[1]["name"], "is a great scientist born in", person[1]["date_of_birth"])
