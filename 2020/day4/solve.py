import re

class Passport():
  def __init__(self, pass_string):
    self.data = {
      "byr": None,
      "iyr": None,
      "eyr": None,
      "hgt": None,
      "hcl": None,
      "ecl": None,
      "pid": None,
      "cid": None
    }
    after_split = re.split("\s", pass_string)
    for s in after_split:
      matche = re.match('(?P<key>\w+):(?P<val>#?\w+)', s)
      self.data[matche.group("key")] = matche.group("val")

  def __byr_v(self):
    if self.data["byr"] is None:
      return False
    return 1920 <= int(self.data["byr"]) <= 2002

  def __iyr_v(self):
    if self.data["iyr"] is None:
      return False
    return 2010 <= int(self.data["iyr"]) <= 2020

  def __eyr_v(self):
    if self.data["eyr"] is None:
      return False
    return 2020 <= int(self.data["eyr"]) <= 2030

  def __hgt_v(self):
    if self.data["hgt"] is None:
      return False
    m = re.match("(?P<val>\d+)(?P<unit>\w+)", self.data["hgt"])
    if m is None:
      return False
    if m.group("unit") == "cm":
      return 150 <= int(m.group("val")) <= 193
    if m.group("unit") == "in":
      return 59 <= int(m.group("val")) <= 76
    return False

  def __hcl_v(self):
    if self.data["hcl"] is None:
      return False
    m = re.match("#[0-9a-fA-F]{6}\Z", self.data["hcl"])
    if m is None:
      return False
    return True

  def __ecl_v(self):
    if self.data["ecl"] is None:
      return False
    possible = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return self.data["ecl"] in possible

  def __pid_v(self):
    if self.data["pid"] is None:
      return False
    m = re.match("\d{9}\Z", self.data["pid"])
    if m is None:
      return False
    return True

  def __cid_v(self):
    return True

  def matches_rules(self):
    validators = {
      "byr": self.__byr_v,
      "iyr": self.__iyr_v,
      "eyr": self.__eyr_v,
      "hgt": self.__hgt_v,
      "hcl": self.__hcl_v,
      "ecl": self.__ecl_v,
      "pid": self.__pid_v,
      "cid": self.__cid_v
    }
    for v in validators:
      if not validators[v]():
        return False
    return True

  def is_valid(self):
    to_ignore = ["cid"]
    for p in self.data:
      if self.data[p] == None:
        if p in to_ignore:
          continue
        return False
    return True
        

with open("day4/input.txt", "r") as f:
  pasports_str = f.read().split("\n\n")

pasports = [Passport(s) for s in pasports_str]

valid = 0
for p in pasports:
  valid += 1 if p.is_valid() else 0

print("Valid#1: {0}".format(valid))

valid = 0
for p in pasports:
  valid += 1 if p.matches_rules() else 0

print("Valid#2: {0}".format(valid))

