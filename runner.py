from auto_diff import *

def main():
    dag = Graph()

    v_0 = Variable(2,'x')
    v_1 = Variable(5,'y')
    v_2 = Log(v_0) + v_0*v_1 - Sin(v_1)

    print("Forward Pass = ",forward_pass())
    backward_pass()

    for node in dag.nodes:
        if isinstance(node, Variable):
            print(f"d/d{node.id} = ", node.gradient)

if __name__ == "__main__":
    main()