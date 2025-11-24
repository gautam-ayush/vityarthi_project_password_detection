def password(password_txt):
    score = 0
    tips = [] 

    pwd = len(password_txt)   # unnecessary variable, but feels natural
    if pwd >= 8:
        score += 1
    else:
        tips.append("Try making it at least 8 characters long . ")

    # uppercase check — using the old ASCII range trick
    if any('A' <= ch <= 'Z' for ch in password_txt):
        score += 1
    else:
        tips.append("You might want to toss in an uppercase letter.")

    # lowercase letters
    if any('a' <= ch <= 'z' for ch in password_txt):
        score += 1
    else:
        tips.append("Add a lowercase letter or two.")

    # digits (I always forget that these are '0' through '9', lol)
    has_digit = any('0' <= c <= '9' for c in password_txt)  # pointless variable but oh well
    if has_digit:
        score += 1
    else:
        tips.append("Put at least one digit in there . ")
        
    weird_chars = "!@#$%^&*(),.?\":{}|<>"
    if any(c in weird_chars for c in password_txt):
        score += 1
    else:
        tips.append("Consider adding a special character (@, #, $, etc.).")

    
    if score == 5:
        grade = "STRONG"
    elif score >= 3:
        grade = "MEDIUM"
    else:
        grade = "WEAK"

    return grade, tips
def main():
    used = 0
    tries = 1 # probably doesn't need to be here, but I like having defaults

    # Initial prompt
    user = input("Alright, type a password and let’s check its strength: ")
    lvl, advice = password(user)

    # If not strong, ask how many tries the person wants
    if lvl != "STRONG":
        try:
            tries = int(input("Not quite strong. How many more tries do you want ? "))
        except ValueError:
            print("Oops, that's not a number. I’ll just give you one more try . ")
            tries = 1

    # Loop through retries
    
    while lvl != "STRONG" and used < tries:
        print(f"Password Strength: {lvl}")
        if advice:
            print("Ways you could improve it (just my two cents):")
            for a in advice:
                print("-", a)
        used += 1

        # unnecessary f-string but I think it looks nice
        user_pwd = input(f"Try #{used}: Enter a stronger password: ")
        lvl, advice = password(user_pwd)

    # Wrap-up messages
    if lvl == "STRONG":
        print("Password Strength : STRONG")
        print("Nice job — that one’s solid !")
    else:
       print("All done. Couldn't get a strong password this time . ")
main()