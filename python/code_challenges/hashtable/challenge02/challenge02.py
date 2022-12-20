def repeated(s):

    mp = {}
    t = ""
    ans = ""

    for i in range(len(s) - 1, -1, -1):

        if (s[i] != ' '):
            t += s[i]

        else:

            if (t in mp):
                ans = t
            else:
                mp[t] = 1

            t = ""

    if (t in mp):
        ans = t

    if (ans != ""):

        ans = ans[::-1]
        return ans
    else:
        return "No Repetition"


a = "ASAC is a department at LTUC. ASAC teaches programming in LTUC."
b = "I am learning programming at ASAC."

repeated(a)
repeated(b)