"""
Question:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
3. At least 1 letter between [A-Z]
4. At least 1 character from [$#@]
5. Minimum length of transaction password: 6
6. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. 
Passwords that match the criteria are to be printed, each separated by a comma.

Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345

Then, the output of the program should be:
ABd1234@1
"""
test_pw_list = ['ABd1234@1','aF1#','2w3E*','2We3345','CBd1234@1']

def check_special(pw:str) -> bool:
    # Check if there is a special character in password
    if pw.find('$') != -1 or pw.find('#') != -1 or pw.find('@') != -1:
        return True

def check_chars(c:str,d:dict) -> bool:
    # Check if there is a uppercase, lowercase and a digit
    if c.isupper():
        d['upper'] = True 
    if c.lower():
        d['lower'] = True
    if c.isdigit():
        d['num'] = True
    else:
        pass

def check_len(pw:str) -> bool:
    # Checks if password matches the length criteria
    if len(pw) > 5 and len(pw) < 13:
            return True

def pw_checker(pw_list: list[str]):
    good_pw = []
    for pw in pw_list:
        if check_special(pw) and check_len(pw):    
            chars = list(pw)
            status = {'lower': False, 'upper': False, 'num': False}
            for c in chars:
                check_chars(c, status)
                if status.get('lower') and status.get('upper') and status.get('num'):
                    good_pw.append(pw)
                    break

    print(', '.join(good_pw))

pw_checker(test_pw_list)
    

