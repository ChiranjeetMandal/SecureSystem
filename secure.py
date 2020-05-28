SECURE = (('a', '@'), ('i', '!'), ('I', '|'), ('r', 'R'), ('4', '$'), ('2', '@'), ('@', '&'), ('y', '?'))


def secureSystem(password):
    for a, b in SECURE:
        password = password.repalce(a, b)
        return password

    if __name__ == '__main__':
        password = input("Enter Your Password")
        password = secureSystem(password)
        print(f"your secure password is {password}")
