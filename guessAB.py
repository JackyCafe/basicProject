from random import randint


def createAns(nums):
    num_array = []
    for i in range(0,10):
        num_array.append(str(i))
    ans = ''
    for j in range(0,nums):
        # print('len of num_array:',len(num_array))
        rand = randint(0,len(num_array)-1)
        # print('rand:',rand)
        ans += num_array[rand]
        num_array.remove(num_array[rand])
    return ans
    # print('ans:',ans)


def compareAB(guess, ans):
    A = 0
    B = 0
    print(ans)
    for i in range(0,len(guess)):
        if guess[i] == ans[i] :
            # print(f'guess{i}: ans.index(guess[{i}])')
            A+=1
        elif ans.find(guess[i])>=0:
            # print(f'guess{i} >> {guess[i]}: {ans.index(guess[i])}')
            B+=1
    return f'{A}A{B}B'



def main():
    ans = createAns(4)
    print(ans)
    guess=input('輸入4位數')
    for i in range(0,10):
        result =compareAB(guess,ans)
        if result == '4A0B':
            print('you win')
            break
        else:
            print(result)
            guess=input('guess again')

        if i == 9:
            print('you are loser')


    print(result)


if __name__ == '__main__':
    main()