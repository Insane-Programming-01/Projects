# Importing the requirements

import random

college = ['FSD Assignments', 'FSD Practicals', 'FSD Microproject', 'Linux Assignments', 'Linux Microproject', 'Linux Practicals', 
            'DSP Assignments', 'DSP Practicals', 'DSP Microproject', 'Seminar', 'Database Assignments', 'Database Practicals', 
            'Database Microproject']
longTasks = ['Go Wired In', 'Machine Learning', 'Youtube Videos', 'Data structures and Algorithms']
selfStudy = ['Read FSD', 'Read DSP', 'Read Database', 'Read Linux', 'Rivise a topic', 'Make Notes']

while True:

    outer = input('\nCOLLEGE / LONG / SELF / EXIT - ').lower()

    if outer == 'college':

        while True:
        
            inner = input('\nADD / DELETE / GET / ALL / EXIT - ').lower()

            if inner == 'add':
                
                value = input('Enter the task - ')

                if value in college:
                    print('Task already there')
                else:
                    college.append(value)
                    print('Task added!')

            elif inner == 'delete':
                
                value = input('Enter the task - ')

                if value in college:
                    college.remove(value)
                    print('Task deleted!')
                else:
                    print('Task not found')
            
            elif inner == 'get':

                # task = random.choice(college)

                task = college[random.randint(0,len(college))]
                print(f'Task - {task}')

            elif inner == 'all':
                print(college)

            elif inner == 'exit':
                break

            else:
                print('\nInvalid Input')

    elif outer == 'long':
        while True:
        
            inner = input('\nADD / DELETE / GET / ALL / EXIT - ').lower()

            if inner == 'add':
                
                value = input('Enter the task - ')

                if value in longTasks:
                    print('Task already there')
                else:
                    longTasks.append(value)
                    print('Task added!')

            elif inner == 'delete':
                
                value = input('Enter the task - ')

                if value in longTasks:
                    longTasks.remove(value)
                    print('Task deleted!')
                else:
                    print('Task not found')
            
            elif inner == 'get':

                # task = random.choice(college)

                task = longTasks[random.randint(0,len(longTasks))]
                print(f'Task - {task}')

            elif inner == 'all':
                print(longTasks)

            elif inner == 'exit':
                break

            else:
                print('\nInvalid Input')
    elif outer == 'self':
        while True:
        
            inner = input('\nADD / DELETE / GET / ALL / EXIT - ').lower()

            if inner == 'add':
                
                value = input('Enter the task - ')

                if value in selfStudy:
                    print('Task already there')
                else:
                    selfStudy.append(value)
                    print('Task added!')

            elif inner == 'delete':
                
                value = input('Enter the task - ')

                if value in selfStudy:
                    selfStudy.remove(value)
                    print('Task deleted!')
                else:
                    print('Task not found')
            
            elif inner == 'get':

                # task = random.choice(college)

                task = selfStudy[random.randint(0,len(selfStudy))]
                print(f'Task - {task}')

            elif inner == 'all':
                print(selfStudy)

            elif inner == 'exit':
                break

            else:
                print('\nInvalid Input')
    elif outer == 'exit':
        break
    else:
        print('\nInvalid input by user.')