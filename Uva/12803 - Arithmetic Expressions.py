from sys import stdin


##Author: Iván Camilo Rincón Saavedra

"""
Función que se encarga de la solución del problema
"""
def main():
    n = int( stdin.readline().strip() )
    for x in range( n ) :
        string = stdin.readline().strip().split()
        left, current = -1, len( string )
        right = -1 
        while( (")" in string) or ( current >= 0 ) ):
            current -= 1
            
            if( left != -1 and right != -1 ):
                op = string[left + 2  ]
                op1, op2 = float( string[left+1] ), float( string[left+3] )
                if( op == "+" ):
                    string[left:right + 1] = [str(op1+op2)]
                    
                elif( op == "-"):
                    string[left:right + 1] = [str(op1-op2)]
                elif( op == "*"):
                    string[left:right + 1] = [str(op1*op2)]
                else:
                    string[left:right + 1] = [str(op1/op2)]
                        
                    
                left, right = -1, -1
                current = len( string ) - 1
                    
            if( string[current] == ")"):
                right = current
            elif( string[current] == "(" ):
                left = current

        string[0] = str( round(float( string[0]),2))
        print(string[0]+"0" if (string[0][-2] == ".") else string[0])


         
     
main()
