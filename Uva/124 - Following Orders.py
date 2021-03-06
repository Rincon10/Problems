from sys import stdin

##Author: Iván Camilo Rincón Saavedra



"""
Funcion que se encarga de validar la solucion parcial actual
@Param solp lista, lista que representa la solucion parcial a vallidar
@Return boolean, que dice si la solp es valida 
"""
def valid( solp ):
    global lenght, pairs
    
    if( len( solp ) > 1 ):
        for element in pairs:
            isE1, isE2  = ( element[0] in solp),( element[1] in solp)
            if( isE2 and not( isE1 ) ):
                return False
            if( isE1 and isE2 ):
                index1, index2 = solp.index(element[0]),solp.index(element[1])
                if( index1 > index2 ):
                    
                    return False
    
    return True 



"""
Funcion que se encarga de realizar backTracking con las opciones proporcionadas, mostrandolo a su vez por pantalla
@Param phase int , numero que indicara la fase actual de la solucion parcial 
@Param options list , las opciones a permutar
@Param solp list ,solucion parcial actual
@Param string String, cadena que almacenara la solucion parcial
"""
def backTracking( phase,options , solp ,string ):
    global lenght, pairs

    if ( phase < lenght ):
        for x in range( len( options ) ):
            
            mOptions  = options[:]
            element = mOptions.pop(x)
            
            
            mSolp = solp[:]
            mSolp.append( element )
            
            mString = string[:]
            mString+=element
            

            if( valid( mSolp ) ):
                
                if( phase < (lenght - 1) ):
                    backTracking( phase + 1,mOptions[:] , mSolp[:],mString )
                else:
                    print( mString )

"""
Funcion principal que se encarga de la lectura del problema
"""
def main():
    global lenght, pairs
    
    case = stdin.readline().strip()
    while( case ):
        case = case.split()
        lenght = len( case )
        p, pairs = stdin.readline().strip().split() , []
        while p:
            pairs.append((p[0],p[1]))
            p = p[2:]
        case.sort()
        backTracking( 0,case[:],[],"")
        case = stdin.readline().strip()
        if (case):print("")
        
main()
