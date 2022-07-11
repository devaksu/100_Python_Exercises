"""You are required to write a program to sort the (name, age, height) tuples by ascending order 
where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:

1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.

Example:
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85

Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]"""


def get_data() -> list[tuple[str,int,int]]:
    people = []
    while True:
        human = tuple(map(str,input("Give name, age and score separated with space: ").split()))
        if human:
            people.append(human)
        else:
            break
    
    return people

def sorting(data_list:list[tuple]) -> list[tuple]:
    data_list.sort(key=lambda y: y[2])
    data_list.sort(key=lambda y: y[1])
    data_list.sort(key=lambda y: y[0])
    return data_list

def main():
    data_list = [('Tom', '19', '80'), ('John', '20', '90'), ('Jony', '17', '93'), ('Jony', '17', '91'), ('Json', '21', '85')]
    #data_list = get_data()
    sorted_list = sorting(data_list)
    print(sorted_list)



if __name__ == '__main__':
    main()