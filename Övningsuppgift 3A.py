person = {
    "namn": "Ali",
    "ålder": 34,
    "stad": "Stockholm",
    "hobbies": ["hobby 1", "hobby 2"],
    "skills": {"programming": 2, "it security": 100},
}
# print(person["ålder"])

# person["ålder"] = 29

# person["yrke"] = "elektriker"

# print(person)

print(person["skills"])

for k, v in person.items():
    print(k, v)
