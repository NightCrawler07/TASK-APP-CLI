import sys


def help():
    print("""Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics""")
def load():
    try:
        f = open('task.txt', 'r')
        for line in f:
            if line!="\n":
                p = line.split()
                inc[int(p[0])] = " ".join(p[1:])
    except:
        print("There are no pending tasks!")


def add(id, str):
    f = open('task.txt', 'a')
    f.write(f"{id} {str}\n")
    f.close()
    print(f'Added task: "{str}" with priority {id}')


def ls():
    load()
    incp=sorted(inc.items())
    try:
        k = 1
        for i in incp:
            str=f"{k}. {i[1]} [{i[0]}]"
            sys.stdout.buffer.write(str.encode('utf8'))
            k += 1
        sys.stdout.buffer.write("\n".encode('utf8'))
    except Exception as e:
        raise e
def lst():
    load()
    incp=sorted(inc.items())
    try:
        k = 1
        for i in incp:
            str=f"{k}. {i[1]} [{i[0]}]\n"
            sys.stdout.buffer.write(str.encode('utf8'))
            k += 1
    except Exception as e:
        raise e

def done(num):
    num=int(num)
    load()
    if num>0 and num<=len(inc):
        l = list(inc.values())
        keyl=l[int(num)-1]
        f2 = open('completed.txt', 'a')
        f2.write(f"{keyl}\n")
        f1 = open('task.txt', 'r+')
        f4=open('temp.txt', 'r+')
        for line in f1:
            if keyl not in line and line!='\n':
                f4.write(f"{line}\n")
        f1=open("task.txt","r+")
        f1.truncate(0)
        f1 = open('task.txt', 'r+')
        f4=open('temp.txt', 'r+')
        for line in f4:
            if line!="\n":
                f1.write(line)
                f1.write('\n')
        load()
        compl()
        f5=open("temp.txt","w")
        print("Marked item as done.")
    else:
        print(f"Error: no incomplete item with index #{num} exists.")

def compl():
    try:
        f = open('completed.txt', 'r+')
        pk = 1
        for line in f:
            if line!='\n':
                comp[pk] = line
                pk+=1
    except Exception as e:
        raise e


def printcomp():
    compl()
    for i in comp.keys():
        str=f"{i}. {comp[i]}"
        sys.stdout.buffer.write(str.encode('utf8'))
        


def report():
    try:
        load()
        compl()
        std=f"Pending : {len(inc)}\n"
        sys.stdout.buffer.write(std.encode('utf8'))
        if len(inc) > 0:
            ls()
        sys.stdout.buffer.write("\n".encode('utf8'))
        ltc=f"Completed : {len(comp)}\n"
        sys.stdout.buffer.write(ltc.encode('utf8'))
        if len(comp) > 0:
            printcomp()
    except Exception as e:
        print(e)

def depl(num):
    load()
    num=int(num)
    if num>0 and num<=len(inc):
        l = list(inc.values())
        keyl=l[int(num)-1]
        f1 = open('task.txt', 'r+')
        f4=open('temp.txt', 'r+')
        for line in f1:
            if keyl not in line and line!='\n':
                f4.write(f"{line}\n")
        f1=open("task.txt","r+")
        f1.truncate(0)
        f1 = open('task.txt', 'r+')
        f4=open('temp.txt', 'r+')
        for line in f4:
            if line!="\n":
                f1.write(line)
                f1.write('\n')
        load()
        f5=open("temp.txt","w+")
        print(f"Deleted task #{num}")
    else:
        print(f"Error: task with index #{num} does not exist. Nothing deleted.")

if __name__ == '__main__':
    inc = {}
    comp = {}
    args = sys.argv
    if len(args)>1:
        if args[1] == "help":
            help()
        elif args[1] == "ls":
            lst()
        elif args[1] == "del":
            if len(args)<3:
                print("Error: Missing NUMBER for deleting tasks.")
            else:
                try:
                    k=int(args[2])
                    depl(args[2])
                except:
                    print("Error: Missing NUMBER for deleting tasks.")
        elif args[1] == "done":
            if len(args)<3:
                print("Error: Missing NUMBER for marking tasks as done.")
            else:
                if args[2]!="" and args[2]!='\n':
                    try:
                        k=int(args[2])
                        done(args[2])
                    except:
                        print("Error: Missing NUMBER for marking tasks as done.")
                else:
                    print("Error: Missing NUMBER for marking tasks as done.")
        elif args[1] == "report":
            report()
        elif args[1] == "add":
            if len(args)<3:
                print("Error: Missing tasks string. Nothing added!")
            else:
                if args[3]!="" and args[3]!='\n':
                    add(args[2], args[3])
                else:
                    print("Error: Missing tasks string. Nothing added!")
    else:
        print("""Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics""")
