###Valid Paranthesis

x = "([{({})}]({}))"

def isvalid(s):
  while "()" in s or "[]" in s or "{}" in s :
    s = s.replace("()", "").replace("[]", "").replace("{}", "")
  return s == ""
isvalid(x)