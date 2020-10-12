import sys


def main():
    admin = {'YH','Jacky','Judy'}
    users = set(sys.argv[1:])
    print(users)
    print('交集',admin & users) #交集
    print('聯集',admin | users) #聯集
    print('差集',admin - users)  # 減集
    print('差集',(admin - users) - (admin & users))  # 減集

if __name__ == '__main__':
    main()