import os, ctypes

# ------------------------------------------------------------------------ #
#             P Y T H O N   W R A P E R   O F   l i b B b M m
#
# - generated with bin/c-to-py.py
# - c-header : bbmm.h
# 
#        /!\ ANY MODIFICATION IN THIS FILE WILL BE ERASED /!\
# ------------------------------------------------------------------------ #

# Usefull ctype types:

c_ushort, c_ulong, c_double, c_void_p=  ctypes.c_ushort, ctypes.c_ulong, ctypes.c_double, ctypes.c_void_p

# Usefull BbMm basis types:

c_digit, c_hash= c_ushort, c_ulong

# CArray tools :

def makeCArray( c_type, size, value ):
    Array= c_type * size
    cArray= Array()
    for i in range(size) :
        cArray[i]= (c_type)( value )
    return cArray

def makeCArrayAs( c_type, size, pythonLst ):
    Array= c_type * size
    cArray= Array()
    for i in range(size) :
        cArray[i]= (c_type)( pythonLst[i] )
    return cArray

def readCArray( py_type, c_type, size, arrayPointer ):
    pLst= ctypes.cast(arrayPointer, ctypes.POINTER(c_type))
    return [ (py_type)(pLst[i]) for i in range(size) ]

# Load c-core BbMm librairy : 

bbmmDir= os.path.dirname(os.path.realpath(__file__))
print( f">>>> LOAD LIB: {bbmmDir} <<<" )
core = ctypes.cdll.LoadLibrary( bbmmDir+"/libbbmm.so" )

# bbmm.h wraps :

# BmCode* newBmCode( digit dimention );
newBmCode= core.newBmCode
newBmCode.restype= c_void_p
newBmCode.argtypes= [c_digit]

# BmCode* newBmCode_numbers( digit dimention, digit* numbers );
newBmCode_numbers= core.newBmCode_numbers
newBmCode_numbers.restype= c_void_p
newBmCode_numbers.argtypes= [c_digit, c_void_p]

# BmCode* newBmCode_all( digit dimention, digit defaultValue );
newBmCode_all= core.newBmCode_all
newBmCode_all.restype= c_void_p
newBmCode_all.argtypes= [c_digit, c_digit]

# BmCode* newBmCodeAs( BmCode* model );
newBmCodeAs= core.newBmCodeAs
newBmCodeAs.restype= c_void_p
newBmCodeAs.argtypes= [c_void_p]

# BmCode* BmCode_create( BmCode* self, digit dimention );
BmCode_create= core.BmCode_create
BmCode_create.restype= c_void_p
BmCode_create.argtypes= [c_void_p, c_digit]

# BmCode* BmCode_create_numbers( BmCode* self, digit dimention, digit* numbers );
BmCode_create_numbers= core.BmCode_create_numbers
BmCode_create_numbers.restype= c_void_p
BmCode_create_numbers.argtypes= [c_void_p, c_digit, c_void_p]

# BmCode* BmCode_create_all( BmCode* self, digit dimention, digit defaultValue );
BmCode_create_all= core.BmCode_create_all
BmCode_create_all.restype= c_void_p
BmCode_create_all.argtypes= [c_void_p, c_digit, c_digit]

# BmCode* BmCode_createAs( BmCode* self, BmCode* model );
BmCode_createAs= core.BmCode_createAs
BmCode_createAs.restype= c_void_p
BmCode_createAs.argtypes= [c_void_p, c_void_p]

# BmCode* BmCode_createMerge( BmCode* self, digit numberOfCodes, BmCode ** codes );
BmCode_createMerge= core.BmCode_createMerge
BmCode_createMerge.restype= c_void_p
BmCode_createMerge.argtypes= [c_void_p, c_digit, c_void_p]

# void deleteBmCode( BmCode* instance );
deleteBmCode= core.deleteBmCode
deleteBmCode.restype= c_void_p
deleteBmCode.argtypes= [c_void_p]

# BmCode* BmCode_destroy( BmCode* self );
BmCode_destroy= core.BmCode_destroy
BmCode_destroy.restype= c_void_p
BmCode_destroy.argtypes= [c_void_p]

# digit BmCode_dimention( BmCode* self );
BmCode_dimention= core.BmCode_dimention
BmCode_dimention.restype= c_digit
BmCode_dimention.argtypes= [c_void_p]

# digit BmCode_digit( BmCode* self, digit index );
BmCode_digit= core.BmCode_digit
BmCode_digit.restype= c_digit
BmCode_digit.argtypes= [c_void_p, c_digit]

# digit BmCode_count( BmCode* self, digit value );
BmCode_count= core.BmCode_count
BmCode_count.restype= c_digit
BmCode_count.argtypes= [c_void_p, c_digit]

# hash BmCode_sum( BmCode* self );
BmCode_sum= core.BmCode_sum
BmCode_sum.restype= c_hash
BmCode_sum.argtypes= [c_void_p]

# hash BmCode_product( BmCode* self );
BmCode_product= core.BmCode_product
BmCode_product.restype= c_hash
BmCode_product.argtypes= [c_void_p]

# BmCode* BmCode_reinit( BmCode* self, digit newDimention );
BmCode_reinit= core.BmCode_reinit
BmCode_reinit.restype= c_void_p
BmCode_reinit.argtypes= [c_void_p, c_digit]

# BmCode* BmCode_copy( BmCode* self, BmCode* model );
BmCode_copy= core.BmCode_copy
BmCode_copy.restype= c_void_p
BmCode_copy.argtypes= [c_void_p, c_void_p]

# BmCode* BmCode_copyNumbers( BmCode* self, BmCode* model );
BmCode_copyNumbers= core.BmCode_copyNumbers
BmCode_copyNumbers.restype= c_void_p
BmCode_copyNumbers.argtypes= [c_void_p, c_void_p]

# BmCode* BmCode_redimention( BmCode* self, digit newDimention );
BmCode_redimention= core.BmCode_redimention
BmCode_redimention.restype= c_void_p
BmCode_redimention.argtypes= [c_void_p, c_digit]

# BmCode* BmCode_setAll( BmCode* self, digit value );
BmCode_setAll= core.BmCode_setAll
BmCode_setAll.restype= c_void_p
BmCode_setAll.argtypes= [c_void_p, c_digit]

# BmCode* BmCode_at_set( BmCode* self, digit index, digit value );
BmCode_at_set= core.BmCode_at_set
BmCode_at_set.restype= c_void_p
BmCode_at_set.argtypes= [c_void_p, c_digit, c_digit]

# BmCode* BmCode_at_increment( BmCode* self, digit index, digit value );
BmCode_at_increment= core.BmCode_at_increment
BmCode_at_increment.restype= c_void_p
BmCode_at_increment.argtypes= [c_void_p, c_digit, c_digit]

# BmCode* BmCode_at_decrement( BmCode* self, digit index, digit value );
BmCode_at_decrement= core.BmCode_at_decrement
BmCode_at_decrement.restype= c_void_p
BmCode_at_decrement.argtypes= [c_void_p, c_digit, c_digit]

# BmCode* BmCode_setNumbers( BmCode* self, digit* numbers );
BmCode_setNumbers= core.BmCode_setNumbers
BmCode_setNumbers.restype= c_void_p
BmCode_setNumbers.argtypes= [c_void_p, c_void_p]

# void BmCode_sort( BmCode* self );
BmCode_sort= core.BmCode_sort
BmCode_sort.restype= c_void_p
BmCode_sort.argtypes= [c_void_p]

# void BmCode_switch( BmCode* self, BmCode* anotherCode );
BmCode_switch= core.BmCode_switch
BmCode_switch.restype= c_void_p
BmCode_switch.argtypes= [c_void_p, c_void_p]

# digit BmCode_search( BmCode* self, digit value );
BmCode_search= core.BmCode_search
BmCode_search.restype= c_digit
BmCode_search.argtypes= [c_void_p, c_digit]

# bool BmCode_isEqualTo( BmCode* self, BmCode* another );
BmCode_isEqualTo= core.BmCode_isEqualTo
BmCode_isEqualTo.restype= c_digit
BmCode_isEqualTo.argtypes= [c_void_p, c_void_p]

# bool BmCode_isGreaterThan( BmCode* self, BmCode* another );
BmCode_isGreaterThan= core.BmCode_isGreaterThan
BmCode_isGreaterThan.restype= c_digit
BmCode_isGreaterThan.argtypes= [c_void_p, c_void_p]

# bool BmCode_isSmallerThan( BmCode* self, BmCode* another );
BmCode_isSmallerThan= core.BmCode_isSmallerThan
BmCode_isSmallerThan.restype= c_digit
BmCode_isSmallerThan.argtypes= [c_void_p, c_void_p]

# hash BmCode_keyOf( BmCode* self, BmCode* code );
BmCode_keyOf= core.BmCode_keyOf
BmCode_keyOf.restype= c_hash
BmCode_keyOf.argtypes= [c_void_p, c_void_p]

# BmCode* BmCode_setCode_onKey( BmCode* self, BmCode* configuration, hash key );
BmCode_setCode_onKey= core.BmCode_setCode_onKey
BmCode_setCode_onKey.restype= c_void_p
BmCode_setCode_onKey.argtypes= [c_void_p, c_void_p, c_hash]

# BmCode* BmCode_setCodeFirst( BmCode* self, BmCode* configuration );
BmCode_setCodeFirst= core.BmCode_setCodeFirst
BmCode_setCodeFirst.restype= c_void_p
BmCode_setCodeFirst.argtypes= [c_void_p, c_void_p]

# BmCode* BmCode_setCodeLast( BmCode* self, BmCode* configuration );
BmCode_setCodeLast= core.BmCode_setCodeLast
BmCode_setCodeLast.restype= c_void_p
BmCode_setCodeLast.argtypes= [c_void_p, c_void_p]

# BmCode* BmCode_newBmCodeOnKey( BmCode* self, hash key );
BmCode_newBmCodeOnKey= core.BmCode_newBmCodeOnKey
BmCode_newBmCodeOnKey.restype= c_void_p
BmCode_newBmCodeOnKey.argtypes= [c_void_p, c_hash]

# BmCode* BmCode_newBmCodeFirst( BmCode* self );
BmCode_newBmCodeFirst= core.BmCode_newBmCodeFirst
BmCode_newBmCodeFirst.restype= c_void_p
BmCode_newBmCodeFirst.argtypes= [c_void_p]

# BmCode* BmCode_newBmCodeLast( BmCode* self );
BmCode_newBmCodeLast= core.BmCode_newBmCodeLast
BmCode_newBmCodeLast.restype= c_void_p
BmCode_newBmCodeLast.argtypes= [c_void_p]

# BmCode* BmCode_nextCode( BmCode* self, BmCode* configuration );
BmCode_nextCode= core.BmCode_nextCode
BmCode_nextCode.restype= c_void_p
BmCode_nextCode.argtypes= [c_void_p, c_void_p]

# BmCode* BmCode_previousCode( BmCode* self, BmCode* configuration );
BmCode_previousCode= core.BmCode_previousCode
BmCode_previousCode.restype= c_void_p
BmCode_previousCode.argtypes= [c_void_p, c_void_p]

# bool BmCode_isIncluding( BmCode* self, BmCode* configuration );
BmCode_isIncluding= core.BmCode_isIncluding
BmCode_isIncluding.restype= c_digit
BmCode_isIncluding.argtypes= [c_void_p, c_void_p]

# BmCode* BmCode_newBmCodeMask( BmCode* self, BmCode* mask );
BmCode_newBmCodeMask= core.BmCode_newBmCodeMask
BmCode_newBmCodeMask.restype= c_void_p
BmCode_newBmCodeMask.argtypes= [c_void_p, c_void_p]

# char* BmCode_print( BmCode* self, char* buffer );
BmCode_print= core.BmCode_print
BmCode_print.restype= c_void_p
BmCode_print.argtypes= [c_void_p, c_void_p]

# BmVector* newBmVector( digit dimention );
newBmVector= core.newBmVector
newBmVector.restype= c_void_p
newBmVector.argtypes= [c_digit]

# BmVector* newBmVector_values( digit dimention, double* values );
newBmVector_values= core.newBmVector_values
newBmVector_values.restype= c_void_p
newBmVector_values.argtypes= [c_digit, c_void_p]

# BmVector* newBmVector_all( digit dimention, double value );
newBmVector_all= core.newBmVector_all
newBmVector_all.restype= c_void_p
newBmVector_all.argtypes= [c_digit, c_double]

# BmVector* newBmVectorAs( BmVector* model );
newBmVectorAs= core.newBmVectorAs
newBmVectorAs.restype= c_void_p
newBmVectorAs.argtypes= [c_void_p]

# BmVector* BmVector_create( BmVector* self, digit dimention );
BmVector_create= core.BmVector_create
BmVector_create.restype= c_void_p
BmVector_create.argtypes= [c_void_p, c_digit]

# BmVector* BmVector_create_values( BmVector* self, digit dimention, double* values );
BmVector_create_values= core.BmVector_create_values
BmVector_create_values.restype= c_void_p
BmVector_create_values.argtypes= [c_void_p, c_digit, c_void_p]

# BmVector* BmVector_create_all( BmVector* self, digit dimention, double value );
BmVector_create_all= core.BmVector_create_all
BmVector_create_all.restype= c_void_p
BmVector_create_all.argtypes= [c_void_p, c_digit, c_double]

# BmVector* BmVector_createAs( BmVector* self, BmVector* model );
BmVector_createAs= core.BmVector_createAs
BmVector_createAs.restype= c_void_p
BmVector_createAs.argtypes= [c_void_p, c_void_p]

# BmVector* BmVector_destroy( BmVector* self );
BmVector_destroy= core.BmVector_destroy
BmVector_destroy.restype= c_void_p
BmVector_destroy.argtypes= [c_void_p]

# void deleteBmVector( BmVector* self );
deleteBmVector= core.deleteBmVector
deleteBmVector.restype= c_void_p
deleteBmVector.argtypes= [c_void_p]

# BmVector* BmVector_reinit( BmVector* self, digit newDimention );
BmVector_reinit= core.BmVector_reinit
BmVector_reinit.restype= c_void_p
BmVector_reinit.argtypes= [c_void_p, c_digit]

# BmVector* BmVector_copy( BmVector* self, BmVector* model );
BmVector_copy= core.BmVector_copy
BmVector_copy.restype= c_void_p
BmVector_copy.argtypes= [c_void_p, c_void_p]

# digit BmVector_dimention( BmVector* self );
BmVector_dimention= core.BmVector_dimention
BmVector_dimention.restype= c_digit
BmVector_dimention.argtypes= [c_void_p]

# double BmVector_value( BmVector* self, digit i );
BmVector_value= core.BmVector_value
BmVector_value.restype= c_double
BmVector_value.argtypes= [c_void_p, c_digit]

# BmVector* BmVector_redimention( BmVector* self, digit newDimention );
BmVector_redimention= core.BmVector_redimention
BmVector_redimention.restype= c_void_p
BmVector_redimention.argtypes= [c_void_p, c_digit]

# double BmVector_at_set( BmVector* self, digit i, double value );
BmVector_at_set= core.BmVector_at_set
BmVector_at_set.restype= c_double
BmVector_at_set.argtypes= [c_void_p, c_digit, c_double]

# BmVector* BmVector_setValues( BmVector* self, double* values );
BmVector_setValues= core.BmVector_setValues
BmVector_setValues.restype= c_void_p
BmVector_setValues.argtypes= [c_void_p, c_void_p]

# double BmVector_sum( BmVector* self );
BmVector_sum= core.BmVector_sum
BmVector_sum.restype= c_double
BmVector_sum.argtypes= [c_void_p]

# double BmVector_product( BmVector* self );
BmVector_product= core.BmVector_product
BmVector_product.restype= c_double
BmVector_product.argtypes= [c_void_p]

# bool BmVector_isEqualTo( BmVector* self, BmVector* another );
BmVector_isEqualTo= core.BmVector_isEqualTo
BmVector_isEqualTo.restype= c_digit
BmVector_isEqualTo.argtypes= [c_void_p, c_void_p]

# bool BmVector_isGreaterThan( BmVector* self, BmVector* another );
BmVector_isGreaterThan= core.BmVector_isGreaterThan
BmVector_isGreaterThan.restype= c_digit
BmVector_isGreaterThan.argtypes= [c_void_p, c_void_p]

# bool BmVector_isSmallerThan( BmVector* self, BmVector* another );
BmVector_isSmallerThan= core.BmVector_isSmallerThan
BmVector_isSmallerThan.restype= c_digit
BmVector_isSmallerThan.argtypes= [c_void_p, c_void_p]

# char* BmVector_print( BmVector* self, char* output );
BmVector_print= core.BmVector_print
BmVector_print.restype= c_void_p
BmVector_print.argtypes= [c_void_p, c_void_p]

# char* BmVector_format_print( BmVector* self, char* format, char* buffer );
BmVector_format_print= core.BmVector_format_print
BmVector_format_print.restype= c_void_p
BmVector_format_print.argtypes= [c_void_p, c_void_p, c_void_p]

# BmBench* newBmBench( digit capacity );
newBmBench= core.newBmBench
newBmBench.restype= c_void_p
newBmBench.argtypes= [c_digit]

# BmBench* newBmBench_codeDim_vectorDim( digit capacity, digit codeDim, digit vectorDim );
newBmBench_codeDim_vectorDim= core.newBmBench_codeDim_vectorDim
newBmBench_codeDim_vectorDim.restype= c_void_p
newBmBench_codeDim_vectorDim.argtypes= [c_digit, c_digit, c_digit]

# BmBench* newBmBench_startDigit_value( digit capacity, digit aDigit, double value );
newBmBench_startDigit_value= core.newBmBench_startDigit_value
newBmBench_startDigit_value.restype= c_void_p
newBmBench_startDigit_value.argtypes= [c_digit, c_digit, c_double]

# BmBench* newBmBench_startWithCode_vector( digit capacity, BmCode* newCode, BmVector* newVector );
newBmBench_startWithCode_vector= core.newBmBench_startWithCode_vector
newBmBench_startWithCode_vector.restype= c_void_p
newBmBench_startWithCode_vector.argtypes= [c_digit, c_void_p, c_void_p]

# BmBench* newBmBenchAs( BmBench* model );
newBmBenchAs= core.newBmBenchAs
newBmBenchAs.restype= c_void_p
newBmBenchAs.argtypes= [c_void_p]

# BmBench* BmBench_create( BmBench* self, digit capacity );
BmBench_create= core.BmBench_create
BmBench_create.restype= c_void_p
BmBench_create.argtypes= [c_void_p, c_digit]

# BmBench* BmBench_create_codeDim_vectorDim( BmBench* self, digit capacity, digit codeDim, digit vectorDim );
BmBench_create_codeDim_vectorDim= core.BmBench_create_codeDim_vectorDim
BmBench_create_codeDim_vectorDim.restype= c_void_p
BmBench_create_codeDim_vectorDim.argtypes= [c_void_p, c_digit, c_digit, c_digit]

# BmBench* BmBench_createAs( BmBench* self, BmBench* model );
BmBench_createAs= core.BmBench_createAs
BmBench_createAs.restype= c_void_p
BmBench_createAs.argtypes= [c_void_p, c_void_p]

# BmBench* BmBench_destroy( BmBench* self );
BmBench_destroy= core.BmBench_destroy
BmBench_destroy.restype= c_void_p
BmBench_destroy.argtypes= [c_void_p]

# void deleteBmBench( BmBench* self );
deleteBmBench= core.deleteBmBench
deleteBmBench.restype= c_void_p
deleteBmBench.argtypes= [c_void_p]

# BmBench* BmBench_reinit( BmBench* self, digit capacity );
BmBench_reinit= core.BmBench_reinit
BmBench_reinit.restype= c_void_p
BmBench_reinit.argtypes= [c_void_p, c_digit]

# digit BmBench_size( BmBench* self );
BmBench_size= core.BmBench_size
BmBench_size.restype= c_digit
BmBench_size.argtypes= [c_void_p]

# digit BmBench_codeDimention( BmBench* self );
BmBench_codeDimention= core.BmBench_codeDimention
BmBench_codeDimention.restype= c_digit
BmBench_codeDimention.argtypes= [c_void_p]

# digit BmBench_vectorDimention( BmBench* self );
BmBench_vectorDimention= core.BmBench_vectorDimention
BmBench_vectorDimention.restype= c_digit
BmBench_vectorDimention.argtypes= [c_void_p]

# BmCode* BmBench_codeAt( BmBench* self, digit i );
BmBench_codeAt= core.BmBench_codeAt
BmBench_codeAt.restype= c_void_p
BmBench_codeAt.argtypes= [c_void_p, c_digit]

# BmVector* BmBench_vectorAt( BmBench* self, digit i );
BmBench_vectorAt= core.BmBench_vectorAt
BmBench_vectorAt.restype= c_void_p
BmBench_vectorAt.argtypes= [c_void_p, c_digit]

# digit BmBench_digitAt( BmBench* self, digit i );
BmBench_digitAt= core.BmBench_digitAt
BmBench_digitAt.restype= c_digit
BmBench_digitAt.argtypes= [c_void_p, c_digit]

# double BmBench_valueAt( BmBench* self, digit i );
BmBench_valueAt= core.BmBench_valueAt
BmBench_valueAt.restype= c_double
BmBench_valueAt.argtypes= [c_void_p, c_digit]

# digit BmBench_at_digit( BmBench* self, digit i, digit j );
BmBench_at_digit= core.BmBench_at_digit
BmBench_at_digit.restype= c_digit
BmBench_at_digit.argtypes= [c_void_p, c_digit, c_digit]

# double BmBench_at_value( BmBench* self, digit i, digit j );
BmBench_at_value= core.BmBench_at_value
BmBench_at_value.restype= c_double
BmBench_at_value.argtypes= [c_void_p, c_digit, c_digit]

# void BmBench_resizeCapacity( BmBench* self, digit newCapacity );
BmBench_resizeCapacity= core.BmBench_resizeCapacity
BmBench_resizeCapacity.restype= c_void_p
BmBench_resizeCapacity.argtypes= [c_void_p, c_digit]

# digit BmBench_attachCode_vector( BmBench* self, BmCode* newCode, BmVector* newVector );
BmBench_attachCode_vector= core.BmBench_attachCode_vector
BmBench_attachCode_vector.restype= c_digit
BmBench_attachCode_vector.argtypes= [c_void_p, c_void_p, c_void_p]

# digit BmBench_attachFrontCode_vector( BmBench* self, BmCode* newCode, BmVector* newVector );
BmBench_attachFrontCode_vector= core.BmBench_attachFrontCode_vector
BmBench_attachFrontCode_vector.restype= c_digit
BmBench_attachFrontCode_vector.argtypes= [c_void_p, c_void_p, c_void_p]

# BmCode* BmBench_detach( BmBench* self );
BmBench_detach= core.BmBench_detach
BmBench_detach.restype= c_void_p
BmBench_detach.argtypes= [c_void_p]

# BmCode* BmBench_detachFront( BmBench* self );
BmBench_detachFront= core.BmBench_detachFront
BmBench_detachFront.restype= c_void_p
BmBench_detachFront.argtypes= [c_void_p]

# BmBench* BmBench_increase( BmBench* self, digit number );
BmBench_increase= core.BmBench_increase
BmBench_increase.restype= c_void_p
BmBench_increase.argtypes= [c_void_p, c_digit]

# BmBench* BmBench_increaseFront( BmBench* self, digit number );
BmBench_increaseFront= core.BmBench_increaseFront
BmBench_increaseFront.restype= c_void_p
BmBench_increaseFront.argtypes= [c_void_p, c_digit]

# digit BmBench_attachCode( BmBench* self, BmCode* newItem );
BmBench_attachCode= core.BmBench_attachCode
BmBench_attachCode.restype= c_digit
BmBench_attachCode.argtypes= [c_void_p, c_void_p]

# digit BmBench_attachVector( BmBench* self, BmVector* newItem );
BmBench_attachVector= core.BmBench_attachVector
BmBench_attachVector.restype= c_digit
BmBench_attachVector.argtypes= [c_void_p, c_void_p]

# void BmBench_switch( BmBench* self, BmBench* doppleganger );
BmBench_switch= core.BmBench_switch
BmBench_switch.restype= c_void_p
BmBench_switch.argtypes= [c_void_p, c_void_p]

# digit BmBench_addDigit_value( BmBench* self, digit d, double v );
BmBench_addDigit_value= core.BmBench_addDigit_value
BmBench_addDigit_value.restype= c_digit
BmBench_addDigit_value.argtypes= [c_void_p, c_digit, c_double]

# BmBench* BmBench_at_setDigit( BmBench* self, digit i, digit aDigit );
BmBench_at_setDigit= core.BmBench_at_setDigit
BmBench_at_setDigit.restype= c_void_p
BmBench_at_setDigit.argtypes= [c_void_p, c_digit, c_digit]

# BmBench* BmBench_at_setValue( BmBench* self, digit i, double value );
BmBench_at_setValue= core.BmBench_at_setValue
BmBench_at_setValue.restype= c_void_p
BmBench_at_setValue.argtypes= [c_void_p, c_digit, c_double]

# void BmBench_add_reducted( BmBench* self, BmBench* another, BmCode* mask );
BmBench_add_reducted= core.BmBench_add_reducted
BmBench_add_reducted.restype= c_void_p
BmBench_add_reducted.argtypes= [c_void_p, c_void_p, c_void_p]

# digit BmBench_sort( BmBench* self, fctptr_BmBench_compare compare );
BmBench_sort= core.BmBench_sort
BmBench_sort.restype= c_digit
BmBench_sort.argtypes= [c_void_p, c_void_p]

# digit BmBench_switchAt_at( BmBench* self, digit id1, digit id2 );
BmBench_switchAt_at= core.BmBench_switchAt_at
BmBench_switchAt_at.restype= c_digit
BmBench_switchAt_at.argtypes= [c_void_p, c_digit, c_digit]

# bool BmBench_is_codeGreater( BmBench* self, digit i1, digit i2 );
BmBench_is_codeGreater= core.BmBench_is_codeGreater
BmBench_is_codeGreater.restype= c_digit
BmBench_is_codeGreater.argtypes= [c_void_p, c_digit, c_digit]

# bool BmBench_is_codeSmaller( BmBench* self, digit i1, digit i2 );
BmBench_is_codeSmaller= core.BmBench_is_codeSmaller
BmBench_is_codeSmaller.restype= c_digit
BmBench_is_codeSmaller.argtypes= [c_void_p, c_digit, c_digit]

# bool BmBench_is_vectorGreater( BmBench* self, digit i1, digit i2 );
BmBench_is_vectorGreater= core.BmBench_is_vectorGreater
BmBench_is_vectorGreater.restype= c_digit
BmBench_is_vectorGreater.argtypes= [c_void_p, c_digit, c_digit]

# bool BmBench_is_vectorSmaller( BmBench* self, digit i1, digit i2 );
BmBench_is_vectorSmaller= core.BmBench_is_vectorSmaller
BmBench_is_vectorSmaller.restype= c_digit
BmBench_is_vectorSmaller.argtypes= [c_void_p, c_digit, c_digit]

# char* BmBench_print( BmBench* self, char* output );
BmBench_print= core.BmBench_print
BmBench_print.restype= c_void_p
BmBench_print.argtypes= [c_void_p, c_void_p]

# char* BmBench_printCodes( BmBench* self, char* output );
BmBench_printCodes= core.BmBench_printCodes
BmBench_printCodes.restype= c_void_p
BmBench_printCodes.argtypes= [c_void_p, c_void_p]

# char* BmBench_printNetwork( BmBench* self, char* output );
BmBench_printNetwork= core.BmBench_printNetwork
BmBench_printNetwork.restype= c_void_p
BmBench_printNetwork.argtypes= [c_void_p, c_void_p]

# BmTree* newBmTree( digit binarySpaceSize );
newBmTree= core.newBmTree
newBmTree.restype= c_void_p
newBmTree.argtypes= [c_digit]

# BmTree* newBmTreeWith( BmCode* newSpace );
newBmTreeWith= core.newBmTreeWith
newBmTreeWith.restype= c_void_p
newBmTreeWith.argtypes= [c_void_p]

# BmTree* BmTree_createWhith( BmTree* self, BmCode* input );
BmTree_createWhith= core.BmTree_createWhith
BmTree_createWhith.restype= c_void_p
BmTree_createWhith.argtypes= [c_void_p, c_void_p]

# BmTree* BmTree_destroy( BmTree* self );
BmTree_destroy= core.BmTree_destroy
BmTree_destroy.restype= c_void_p
BmTree_destroy.argtypes= [c_void_p]

# void deleteBmTree( BmTree* self );
deleteBmTree= core.deleteBmTree
deleteBmTree.restype= c_void_p
deleteBmTree.argtypes= [c_void_p]

# BmTree* BmTree_reinitWith( BmTree* self, BmCode* newSpace );
BmTree_reinitWith= core.BmTree_reinitWith
BmTree_reinitWith.restype= c_void_p
BmTree_reinitWith.argtypes= [c_void_p, c_void_p]

# BmTree* BmTree_clearWhith_on( BmTree* self, digit index, digit defaultOption );
BmTree_clearWhith_on= core.BmTree_clearWhith_on
BmTree_clearWhith_on.restype= c_void_p
BmTree_clearWhith_on.argtypes= [c_void_p, c_digit, c_digit]

# BmTree* BmTree_clearOn( BmTree* self, digit defaultOption );
BmTree_clearOn= core.BmTree_clearOn
BmTree_clearOn.restype= c_void_p
BmTree_clearOn.argtypes= [c_void_p, c_digit]

# digit BmTree_dimention( BmTree* self );
BmTree_dimention= core.BmTree_dimention
BmTree_dimention.restype= c_digit
BmTree_dimention.argtypes= [c_void_p]

# digit BmTree_size( BmTree* self );
BmTree_size= core.BmTree_size
BmTree_size.restype= c_digit
BmTree_size.argtypes= [c_void_p]

# BmCode* BmTree_inputRanges( BmTree* self );
BmTree_inputRanges= core.BmTree_inputRanges
BmTree_inputRanges.restype= c_void_p
BmTree_inputRanges.argtypes= [c_void_p]

# digit BmTree_at( BmTree* self, BmCode* code );
BmTree_at= core.BmTree_at
BmTree_at.restype= c_digit
BmTree_at.argtypes= [c_void_p, c_void_p]

# digit BmTreeChild( digit key );
BmTreeChild= core.BmTreeChild
BmTreeChild.restype= c_digit
BmTreeChild.argtypes= [c_digit]

# digit BmTreeLeaf( digit key );
BmTreeLeaf= core.BmTreeLeaf
BmTreeLeaf.restype= c_digit
BmTreeLeaf.argtypes= [c_digit]

# void BmTree_reziseCapacity( BmTree* self, digit newCapacity );
BmTree_reziseCapacity= core.BmTree_reziseCapacity
BmTree_reziseCapacity.restype= c_void_p
BmTree_reziseCapacity.argtypes= [c_void_p, c_digit]

# void BmTree_reziseCompleteCapacity( BmTree* self );
BmTree_reziseCompleteCapacity= core.BmTree_reziseCompleteCapacity
BmTree_reziseCompleteCapacity.restype= c_void_p
BmTree_reziseCompleteCapacity.argtypes= [c_void_p]

# digit BmTree_at_set( BmTree* self, BmCode* code, digit output );
BmTree_at_set= core.BmTree_at_set
BmTree_at_set.restype= c_digit
BmTree_at_set.argtypes= [c_void_p, c_void_p, c_digit]

# digit BmTree_at_readOrder_set( BmTree* self, BmCode* code, BmCode* codeOrder, digit output );
BmTree_at_readOrder_set= core.BmTree_at_readOrder_set
BmTree_at_readOrder_set.restype= c_digit
BmTree_at_readOrder_set.argtypes= [c_void_p, c_void_p, c_void_p, c_digit]

# digit BmTree_branchSize( BmTree* self, digit iBranch );
BmTree_branchSize= core.BmTree_branchSize
BmTree_branchSize.restype= c_digit
BmTree_branchSize.argtypes= [c_void_p, c_digit]

# digit BmTree_branch_stateIndex( BmTree* self, digit iBranch, digit state );
BmTree_branch_stateIndex= core.BmTree_branch_stateIndex
BmTree_branch_stateIndex.restype= c_digit
BmTree_branch_stateIndex.argtypes= [c_void_p, c_digit, c_digit]

# digit BmTree_branch_state( BmTree* self, digit iBranch, digit state );
BmTree_branch_state= core.BmTree_branch_state
BmTree_branch_state.restype= c_digit
BmTree_branch_state.argtypes= [c_void_p, c_digit, c_digit]

# digit BmTree_branch_stateIsLeaf( BmTree* self, digit iBranch, digit state );
BmTree_branch_stateIsLeaf= core.BmTree_branch_stateIsLeaf
BmTree_branch_stateIsLeaf.restype= c_digit
BmTree_branch_stateIsLeaf.argtypes= [c_void_p, c_digit, c_digit]

# digit BmTree_branch_stateOption( BmTree* self, digit iBranch, digit state );
BmTree_branch_stateOption= core.BmTree_branch_stateOption
BmTree_branch_stateOption.restype= c_digit
BmTree_branch_stateOption.argtypes= [c_void_p, c_digit, c_digit]

# digit BmTree_branch_stateLeaf( BmTree* self, digit iBranch, digit state );
BmTree_branch_stateLeaf= core.BmTree_branch_stateLeaf
BmTree_branch_stateLeaf.restype= c_digit
BmTree_branch_stateLeaf.argtypes= [c_void_p, c_digit, c_digit]

# digit BmTree_branchVariable( BmTree* self, digit iBranch );
BmTree_branchVariable= core.BmTree_branchVariable
BmTree_branchVariable.restype= c_digit
BmTree_branchVariable.argtypes= [c_void_p, c_digit]

# digit BmTree_branchStart( BmTree* self, digit iBranch );
BmTree_branchStart= core.BmTree_branchStart
BmTree_branchStart.restype= c_digit
BmTree_branchStart.argtypes= [c_void_p, c_digit]

# digit BmTree_branchBound( BmTree* self, digit iBranch );
BmTree_branchBound= core.BmTree_branchBound
BmTree_branchBound.restype= c_digit
BmTree_branchBound.argtypes= [c_void_p, c_digit]

# digit BmTree_branchStep( BmTree* self, digit iBranch );
BmTree_branchStep= core.BmTree_branchStep
BmTree_branchStep.restype= c_digit
BmTree_branchStep.argtypes= [c_void_p, c_digit]

# digit BmTree_branchNumberOfOutputs( BmTree* self, digit branch );
BmTree_branchNumberOfOutputs= core.BmTree_branchNumberOfOutputs
BmTree_branchNumberOfOutputs.restype= c_digit
BmTree_branchNumberOfOutputs.argtypes= [c_void_p, c_digit]

# digit BmTree_deepOf( BmTree* self, BmCode* code );
BmTree_deepOf= core.BmTree_deepOf
BmTree_deepOf.restype= c_digit
BmTree_deepOf.argtypes= [c_void_p, c_void_p]

# digit BmTree_newBranch( BmTree* self, digit iVariable, digit start, digit bound, digit step );
BmTree_newBranch= core.BmTree_newBranch
BmTree_newBranch.restype= c_digit
BmTree_newBranch.argtypes= [c_void_p, c_digit, c_digit, c_digit, c_digit]

# digit BmTree_newBranch_full( BmTree* self, digit iVariable, digit defaultOption );
BmTree_newBranch_full= core.BmTree_newBranch_full
BmTree_newBranch_full.restype= c_digit
BmTree_newBranch_full.argtypes= [c_void_p, c_digit, c_digit]

# digit BmTree_newBranch_binary_options( BmTree* self, digit iVariable, digit  afterValue, digit option1, digit option2 );
BmTree_newBranch_binary_options= core.BmTree_newBranch_binary_options
BmTree_newBranch_binary_options.restype= c_digit
BmTree_newBranch_binary_options.argtypes= [c_void_p, c_digit, c_void_p, c_digit, c_digit]

# digit BmTree_newBranch_pivot_options( BmTree* self, digit iVariable, digit onValue, digit option1, digit optionOn, digit option2 );
BmTree_newBranch_pivot_options= core.BmTree_newBranch_pivot_options
BmTree_newBranch_pivot_options.restype= c_digit
BmTree_newBranch_pivot_options.argtypes= [c_void_p, c_digit, c_digit, c_digit, c_digit, c_digit]

# void BmTree_branch_state_connect( BmTree* self, digit branchA, digit stateA, digit branchB );
BmTree_branch_state_connect= core.BmTree_branch_state_connect
BmTree_branch_state_connect.restype= c_void_p
BmTree_branch_state_connect.argtypes= [c_void_p, c_digit, c_digit, c_digit]

# void BmTree_branch_state_setOption( BmTree* self, digit branchA, digit iState, digit outbut );
BmTree_branch_state_setOption= core.BmTree_branch_state_setOption
BmTree_branch_state_setOption.restype= c_void_p
BmTree_branch_state_setOption.argtypes= [c_void_p, c_digit, c_digit, c_digit]

# digit BmTree_cleanDeadBranches( BmTree* self );
BmTree_cleanDeadBranches= core.BmTree_cleanDeadBranches
BmTree_cleanDeadBranches.restype= c_digit
BmTree_cleanDeadBranches.argtypes= [c_void_p]

# digit BmTree_removeBranch( BmTree* self, digit iBranch );
BmTree_removeBranch= core.BmTree_removeBranch
BmTree_removeBranch.restype= c_digit
BmTree_removeBranch.argtypes= [c_void_p, c_digit]

# BmBench* BmTree_asNewBench( BmTree* self );
BmTree_asNewBench= core.BmTree_asNewBench
BmTree_asNewBench.restype= c_void_p
BmTree_asNewBench.argtypes= [c_void_p]

# void BmTree_fromBench( BmTree* self, BmBench* model );
BmTree_fromBench= core.BmTree_fromBench
BmTree_fromBench.restype= c_void_p
BmTree_fromBench.argtypes= [c_void_p, c_void_p]

# char* BmTree_branch_print( BmTree* self, digit iBranch, char* output );
BmTree_branch_print= core.BmTree_branch_print
BmTree_branch_print.restype= c_void_p
BmTree_branch_print.argtypes= [c_void_p, c_digit, c_void_p]

# char* BmTree_print( BmTree* self, char* output );
BmTree_print= core.BmTree_print
BmTree_print.restype= c_void_p
BmTree_print.argtypes= [c_void_p, c_void_p]

# char* BmTree_print_sep( BmTree* self, char* output, char* separator );
BmTree_print_sep= core.BmTree_print_sep
BmTree_print_sep.restype= c_void_p
BmTree_print_sep.argtypes= [c_void_p, c_void_p, c_void_p]

# char* BmTree_print( BmTree* self, char* output );
BmTree_print= core.BmTree_print
BmTree_print.restype= c_void_p
BmTree_print.argtypes= [c_void_p, c_void_p]

# char* BmTree_printInside( BmTree* self, char* output );
BmTree_printInside= core.BmTree_printInside
BmTree_printInside.restype= c_void_p
BmTree_printInside.argtypes= [c_void_p, c_void_p]

# BmValueFct* newBmValueFctBasic( digit inputSize, digit outputSize );
newBmValueFctBasic= core.newBmValueFctBasic
newBmValueFctBasic.restype= c_void_p
newBmValueFctBasic.argtypes= [c_digit, c_digit]

# BmValueFct* newBmValueFctWith( BmCode* newInputRanges, BmVector* newOutputs );
newBmValueFctWith= core.newBmValueFctWith
newBmValueFctWith.restype= c_void_p
newBmValueFctWith.argtypes= [c_void_p, c_void_p]

# BmValueFct* BmValueFct_createWith( BmValueFct* self, BmCode* newInputRanges, BmVector* newOutputs );
BmValueFct_createWith= core.BmValueFct_createWith
BmValueFct_createWith.restype= c_void_p
BmValueFct_createWith.argtypes= [c_void_p, c_void_p, c_void_p]

# BmValueFct* BmValueFct_destroy( BmValueFct* self );
BmValueFct_destroy= core.BmValueFct_destroy
BmValueFct_destroy.restype= c_void_p
BmValueFct_destroy.argtypes= [c_void_p]

# void deleteBmValueFct( BmValueFct* instance );
deleteBmValueFct= core.deleteBmValueFct
deleteBmValueFct.restype= c_void_p
deleteBmValueFct.argtypes= [c_void_p]

# digit BmValueFct_reinitWith( BmValueFct* self, BmCode* newInputRanges, BmVector* newOutputs );
BmValueFct_reinitWith= core.BmValueFct_reinitWith
BmValueFct_reinitWith.restype= c_digit
BmValueFct_reinitWith.argtypes= [c_void_p, c_void_p, c_void_p]

# BmTree* BmValueFct_selector( BmValueFct* self );
BmValueFct_selector= core.BmValueFct_selector
BmValueFct_selector.restype= c_void_p
BmValueFct_selector.argtypes= [c_void_p]

# digit BmValueFct_inputDimention( BmValueFct* self );
BmValueFct_inputDimention= core.BmValueFct_inputDimention
BmValueFct_inputDimention.restype= c_digit
BmValueFct_inputDimention.argtypes= [c_void_p]

# digit BmValueFct_outputSize( BmValueFct* self );
BmValueFct_outputSize= core.BmValueFct_outputSize
BmValueFct_outputSize.restype= c_digit
BmValueFct_outputSize.argtypes= [c_void_p]

# BmCode* BmValueFct_inputRanges( BmValueFct* self );
BmValueFct_inputRanges= core.BmValueFct_inputRanges
BmValueFct_inputRanges.restype= c_void_p
BmValueFct_inputRanges.argtypes= [c_void_p]

# BmVector* BmValueFct_outputs( BmValueFct* self );
BmValueFct_outputs= core.BmValueFct_outputs
BmValueFct_outputs.restype= c_void_p
BmValueFct_outputs.argtypes= [c_void_p]

# double BmValueFct_from( BmValueFct* self, BmCode* input );
BmValueFct_from= core.BmValueFct_from
BmValueFct_from.restype= c_double
BmValueFct_from.argtypes= [c_void_p, c_void_p]

# digit BmValueFct_addValue( BmValueFct* self, double ouputValue );
BmValueFct_addValue= core.BmValueFct_addValue
BmValueFct_addValue.restype= c_digit
BmValueFct_addValue.argtypes= [c_void_p, c_double]

# digit BmValueFct_ouputId_setValue( BmValueFct* self, digit ouputId, double ouputValue );
BmValueFct_ouputId_setValue= core.BmValueFct_ouputId_setValue
BmValueFct_ouputId_setValue.restype= c_digit
BmValueFct_ouputId_setValue.argtypes= [c_void_p, c_digit, c_double]

# digit BmValueFct_from_set( BmValueFct* self, BmCode* input, digit ouputId );
BmValueFct_from_set= core.BmValueFct_from_set
BmValueFct_from_set.restype= c_digit
BmValueFct_from_set.argtypes= [c_void_p, c_void_p, c_digit]

# void BmValueFct_switch( BmValueFct* self, BmValueFct* doppelganger );
BmValueFct_switch= core.BmValueFct_switch
BmValueFct_switch.restype= c_void_p
BmValueFct_switch.argtypes= [c_void_p, c_void_p]

# BmBench* BmValueFct_asNewBench( BmValueFct* self );
BmValueFct_asNewBench= core.BmValueFct_asNewBench
BmValueFct_asNewBench.restype= c_void_p
BmValueFct_asNewBench.argtypes= [c_void_p]

# char* BmValueFct_print( BmValueFct* self, char* buffer );
BmValueFct_print= core.BmValueFct_print
BmValueFct_print.restype= c_void_p
BmValueFct_print.argtypes= [c_void_p, c_void_p]

# char* BmValueFct_printSep( BmValueFct* self, char* buffer, char* separator );
BmValueFct_printSep= core.BmValueFct_printSep
BmValueFct_printSep.restype= c_void_p
BmValueFct_printSep.argtypes= [c_void_p, c_void_p, c_void_p]

# BmFunction* newBmFunctionBasic( digit inputSize );
newBmFunctionBasic= core.newBmFunctionBasic
newBmFunctionBasic.restype= c_void_p
newBmFunctionBasic.argtypes= [c_digit]

# BmFunction* newBmFunctionWith( BmCode* newInputRanges, BmBench* newOutputs );
newBmFunctionWith= core.newBmFunctionWith
newBmFunctionWith.restype= c_void_p
newBmFunctionWith.argtypes= [c_void_p, c_void_p]

# BmFunction* BmFunction_createWith( BmFunction* self, BmCode* newInputRanges, BmBench* newOutputs );
BmFunction_createWith= core.BmFunction_createWith
BmFunction_createWith.restype= c_void_p
BmFunction_createWith.argtypes= [c_void_p, c_void_p, c_void_p]

# BmFunction* BmFunction_destroy( BmFunction* self );
BmFunction_destroy= core.BmFunction_destroy
BmFunction_destroy.restype= c_void_p
BmFunction_destroy.argtypes= [c_void_p]

# void deleteBmFunction( BmFunction* instance );
deleteBmFunction= core.deleteBmFunction
deleteBmFunction.restype= c_void_p
deleteBmFunction.argtypes= [c_void_p]

# BmFunction* BmFunction_reinitWith( BmFunction* self, BmCode* newInputRanges, BmBench* newOutputs );
BmFunction_reinitWith= core.BmFunction_reinitWith
BmFunction_reinitWith.restype= c_void_p
BmFunction_reinitWith.argtypes= [c_void_p, c_void_p, c_void_p]

# BmFunction* BmFunction_reinitWithDefault( BmFunction* self, BmCode* newInputRanges, BmCode* newDefaultOutput, double defaultValue );
BmFunction_reinitWithDefault= core.BmFunction_reinitWithDefault
BmFunction_reinitWithDefault.restype= c_void_p
BmFunction_reinitWithDefault.argtypes= [c_void_p, c_void_p, c_void_p, c_double]

# BmTree* BmFunction_selector( BmFunction* self );
BmFunction_selector= core.BmFunction_selector
BmFunction_selector.restype= c_void_p
BmFunction_selector.argtypes= [c_void_p]

# digit BmFunction_inputDimention( BmFunction* self );
BmFunction_inputDimention= core.BmFunction_inputDimention
BmFunction_inputDimention.restype= c_digit
BmFunction_inputDimention.argtypes= [c_void_p]

# BmCode* BmFunction_inputRanges( BmFunction* self );
BmFunction_inputRanges= core.BmFunction_inputRanges
BmFunction_inputRanges.restype= c_void_p
BmFunction_inputRanges.argtypes= [c_void_p]

# digit BmFunction_outputSize( BmFunction* self );
BmFunction_outputSize= core.BmFunction_outputSize
BmFunction_outputSize.restype= c_digit
BmFunction_outputSize.argtypes= [c_void_p]

# BmBench* BmFunction_outputs( BmFunction* self );
BmFunction_outputs= core.BmFunction_outputs
BmFunction_outputs.restype= c_void_p
BmFunction_outputs.argtypes= [c_void_p]

# digit BmFunction_from( BmFunction* self, BmCode* input );
BmFunction_from= core.BmFunction_from
BmFunction_from.restype= c_digit
BmFunction_from.argtypes= [c_void_p, c_void_p]

# BmCode* BmFunction_codeFrom( BmFunction* self, BmCode* input );
BmFunction_codeFrom= core.BmFunction_codeFrom
BmFunction_codeFrom.restype= c_void_p
BmFunction_codeFrom.argtypes= [c_void_p, c_void_p]

# double BmFunction_valueFrom( BmFunction* self, BmCode* input );
BmFunction_valueFrom= core.BmFunction_valueFrom
BmFunction_valueFrom.restype= c_double
BmFunction_valueFrom.argtypes= [c_void_p, c_void_p]

# digit BmFunction_attachOuput( BmFunction* self, BmCode* newOuputCode, double ouputValue );
BmFunction_attachOuput= core.BmFunction_attachOuput
BmFunction_attachOuput.restype= c_digit
BmFunction_attachOuput.argtypes= [c_void_p, c_void_p, c_double]

# digit BmFunction_from_set( BmFunction* self, BmCode* input, digit ouputId );
BmFunction_from_set= core.BmFunction_from_set
BmFunction_from_set.restype= c_digit
BmFunction_from_set.argtypes= [c_void_p, c_void_p, c_digit]

# void BmFunction_switch( BmFunction* self, BmFunction* doppelganger );
BmFunction_switch= core.BmFunction_switch
BmFunction_switch.restype= c_void_p
BmFunction_switch.argtypes= [c_void_p, c_void_p]

# char* BmFunction_print( BmFunction* self, char* output );
BmFunction_print= core.BmFunction_print
BmFunction_print.restype= c_void_p
BmFunction_print.argtypes= [c_void_p, c_void_p]

# char* BmFunction_printSep( BmFunction* self, char* output, char* separator );
BmFunction_printSep= core.BmFunction_printSep
BmFunction_printSep.restype= c_void_p
BmFunction_printSep.argtypes= [c_void_p, c_void_p, c_void_p]

# BmCondition* newBmConditionBasic( digit domain );
newBmConditionBasic= core.newBmConditionBasic
newBmConditionBasic.restype= c_void_p
newBmConditionBasic.argtypes= [c_digit]

# BmCondition* newBmConditionWith( digit domain, BmCode* newInputRanges, BmBench* newDefaultDistrib );
newBmConditionWith= core.newBmConditionWith
newBmConditionWith.restype= c_void_p
newBmConditionWith.argtypes= [c_digit, c_void_p, c_void_p]

# BmCondition* BmCondition_createBasic( BmCondition* self, digit domain );
BmCondition_createBasic= core.BmCondition_createBasic
BmCondition_createBasic.restype= c_void_p
BmCondition_createBasic.argtypes= [c_void_p, c_digit]

# BmCondition* BmCondition_createWith( BmCondition* self, digit domain, BmCode* newInputRanges, BmBench* newDefaultDistrib );
BmCondition_createWith= core.BmCondition_createWith
BmCondition_createWith.restype= c_void_p
BmCondition_createWith.argtypes= [c_void_p, c_digit, c_void_p, c_void_p]

# BmCondition* BmCondition_destroy( BmCondition* self );
BmCondition_destroy= core.BmCondition_destroy
BmCondition_destroy.restype= c_void_p
BmCondition_destroy.argtypes= [c_void_p]

# void deleteBmCondition( BmCondition* instance );
deleteBmCondition= core.deleteBmCondition
deleteBmCondition.restype= c_void_p
deleteBmCondition.argtypes= [c_void_p]

# digit BmCondition_reinitWith( BmCondition* self, digit domain, BmCode* newInputRanges, BmBench* newDistrib );
BmCondition_reinitWith= core.BmCondition_reinitWith
BmCondition_reinitWith.restype= c_digit
BmCondition_reinitWith.argtypes= [c_void_p, c_digit, c_void_p, c_void_p]

# digit BmCondition_reinitDistributionsWith( BmCondition* self, BmBench* newDistrib );
BmCondition_reinitDistributionsWith= core.BmCondition_reinitDistributionsWith
BmCondition_reinitDistributionsWith.restype= c_digit
BmCondition_reinitDistributionsWith.argtypes= [c_void_p, c_void_p]

# digit BmCondition_range( BmCondition* self );
BmCondition_range= core.BmCondition_range
BmCondition_range.restype= c_digit
BmCondition_range.argtypes= [c_void_p]

# BmTree* BmCondition_selector( BmCondition* self );
BmCondition_selector= core.BmCondition_selector
BmCondition_selector.restype= c_void_p
BmCondition_selector.argtypes= [c_void_p]

# BmCode* BmCondition_parents( BmCondition* self );
BmCondition_parents= core.BmCondition_parents
BmCondition_parents.restype= c_void_p
BmCondition_parents.argtypes= [c_void_p]

# BmBench* BmCondition_from( BmCondition* self, BmCode* configuration );
BmCondition_from= core.BmCondition_from
BmCondition_from.restype= c_void_p
BmCondition_from.argtypes= [c_void_p, c_void_p]

# BmBench* BmCondition_fromKey( BmCondition* self, digit configKey );
BmCondition_fromKey= core.BmCondition_fromKey
BmCondition_fromKey.restype= c_void_p
BmCondition_fromKey.argtypes= [c_void_p, c_digit]

# digit BmCondition_distributionSize( BmCondition* self );
BmCondition_distributionSize= core.BmCondition_distributionSize
BmCondition_distributionSize.restype= c_digit
BmCondition_distributionSize.argtypes= [c_void_p]

# BmBench* BmCondition_distributionAt( BmCondition* self, digit iDistrib );
BmCondition_distributionAt= core.BmCondition_distributionAt
BmCondition_distributionAt.restype= c_void_p
BmCondition_distributionAt.argtypes= [c_void_p, c_digit]

# digit BmCondition_attach( BmCondition* self, BmBench* distribution );
BmCondition_attach= core.BmCondition_attach
BmCondition_attach.restype= c_digit
BmCondition_attach.argtypes= [c_void_p, c_void_p]

# digit BmCondition_from_attach( BmCondition* self, BmCode* configuration, BmBench* distribution );
BmCondition_from_attach= core.BmCondition_from_attach
BmCondition_from_attach.restype= c_digit
BmCondition_from_attach.argtypes= [c_void_p, c_void_p, c_void_p]

# void BmCondition_switch( BmCondition* self, BmCondition* doppelganger );
BmCondition_switch= core.BmCondition_switch
BmCondition_switch.restype= c_void_p
BmCondition_switch.argtypes= [c_void_p, c_void_p]

# BmBench* BmCondition_infer( BmCondition* self, BmBench* distribOverConfigurations );
BmCondition_infer= core.BmCondition_infer
BmCondition_infer.restype= c_void_p
BmCondition_infer.argtypes= [c_void_p, c_void_p]

# BmBench* BmCondition_newDistributionByInfering( BmCondition* self, BmBench* distribOverConfigurations );
BmCondition_newDistributionByInfering= core.BmCondition_newDistributionByInfering
BmCondition_newDistributionByInfering.restype= c_void_p
BmCondition_newDistributionByInfering.argtypes= [c_void_p, c_void_p]

# BmBench* BmCondition_newDistributionByInfering_mask( BmCondition* self, BmBench* longDistrib, BmCode* parentMask );
BmCondition_newDistributionByInfering_mask= core.BmCondition_newDistributionByInfering_mask
BmCondition_newDistributionByInfering_mask.restype= c_void_p
BmCondition_newDistributionByInfering_mask.argtypes= [c_void_p, c_void_p, c_void_p]

# char* BmCondition_print( BmCondition* self, char* output );
BmCondition_print= core.BmCondition_print
BmCondition_print.restype= c_void_p
BmCondition_print.argtypes= [c_void_p, c_void_p]

# char* BmCondition_printSep( BmCondition* self, char* output, char* separator );
BmCondition_printSep= core.BmCondition_printSep
BmCondition_printSep.restype= c_void_p
BmCondition_printSep.argtypes= [c_void_p, c_void_p, c_void_p]

# char* BmCondition_printExtend( BmCondition* self, char* output );
BmCondition_printExtend= core.BmCondition_printExtend
BmCondition_printExtend.restype= c_void_p
BmCondition_printExtend.argtypes= [c_void_p, c_void_p]

# char* BmCondition_printExtendSep( BmCondition* self, char* output, char* separator );
BmCondition_printExtendSep= core.BmCondition_printExtendSep
BmCondition_printExtendSep.restype= c_void_p
BmCondition_printExtendSep.argtypes= [c_void_p, c_void_p, c_void_p]

# char* BmCondition_printIdentity( BmCondition* self, char* output );
BmCondition_printIdentity= core.BmCondition_printIdentity
BmCondition_printIdentity.restype= c_void_p
BmCondition_printIdentity.argtypes= [c_void_p, c_void_p]

# BmInferer* newBmInferer( BmCode* variableSpace, digit inputDimention, digit outputDimention );
newBmInferer= core.newBmInferer
newBmInferer.restype= c_void_p
newBmInferer.argtypes= [c_void_p, c_digit, c_digit]

# BmInferer* newBmInfererStateAction( BmCode* stateSpace, BmCode* actionSpace );
newBmInfererStateAction= core.newBmInfererStateAction
newBmInfererStateAction.restype= c_void_p
newBmInfererStateAction.argtypes= [c_void_p, c_void_p]

# BmInferer* newBmInfererStateActionShift( BmCode* stateSpace, BmCode* actionSpace, BmCode* shiftSpace );
newBmInfererStateActionShift= core.newBmInfererStateActionShift
newBmInfererStateActionShift.restype= c_void_p
newBmInfererStateActionShift.argtypes= [c_void_p, c_void_p, c_void_p]

# BmInferer* BmInferer_create( BmInferer* self, BmCode* varDomains, digit inputDimention, digit outputDimention );
BmInferer_create= core.BmInferer_create
BmInferer_create.restype= c_void_p
BmInferer_create.argtypes= [c_void_p, c_void_p, c_digit, c_digit]

# BmInferer* BmInferer_destroy( BmInferer* self );
BmInferer_destroy= core.BmInferer_destroy
BmInferer_destroy.restype= c_void_p
BmInferer_destroy.argtypes= [c_void_p]

# void deleteBmInferer( BmInferer* self );
deleteBmInferer= core.deleteBmInferer
deleteBmInferer.restype= c_void_p
deleteBmInferer.argtypes= [c_void_p]

# BmBench* BmInferer_distribution( BmInferer* self );
BmInferer_distribution= core.BmInferer_distribution
BmInferer_distribution.restype= c_void_p
BmInferer_distribution.argtypes= [c_void_p]

# digit BmInferer_inputDimention( BmInferer* self );
BmInferer_inputDimention= core.BmInferer_inputDimention
BmInferer_inputDimention.restype= c_digit
BmInferer_inputDimention.argtypes= [c_void_p]

# digit BmInferer_outputDimention( BmInferer* self );
BmInferer_outputDimention= core.BmInferer_outputDimention
BmInferer_outputDimention.restype= c_digit
BmInferer_outputDimention.argtypes= [c_void_p]

# digit BmInferer_shiftDimention( BmInferer* self );
BmInferer_shiftDimention= core.BmInferer_shiftDimention
BmInferer_shiftDimention.restype= c_digit
BmInferer_shiftDimention.argtypes= [c_void_p]

# digit BmInferer_overallDimention( BmInferer* self );
BmInferer_overallDimention= core.BmInferer_overallDimention
BmInferer_overallDimention.restype= c_digit
BmInferer_overallDimention.argtypes= [c_void_p]

# BmCondition* BmInferer_node( BmInferer* self, digit iNode );
BmInferer_node= core.BmInferer_node
BmInferer_node.restype= c_void_p
BmInferer_node.argtypes= [c_void_p, c_digit]

# digit BmInferer_node_size( BmInferer* self, digit iVar );
BmInferer_node_size= core.BmInferer_node_size
BmInferer_node_size.restype= c_digit
BmInferer_node_size.argtypes= [c_void_p, c_digit]

# BmCode* BmInferer_node_parents( BmInferer* self, digit iVar );
BmInferer_node_parents= core.BmInferer_node_parents
BmInferer_node_parents.restype= c_void_p
BmInferer_node_parents.argtypes= [c_void_p, c_digit]

# BmCondition* BmInferer_reinitIndependantNode( BmInferer* self, digit index );
BmInferer_reinitIndependantNode= core.BmInferer_reinitIndependantNode
BmInferer_reinitIndependantNode.restype= c_void_p
BmInferer_reinitIndependantNode.argtypes= [c_void_p, c_digit]

# BmCondition* BmInferer_node_reinitWith( BmInferer* self, digit index, BmCode* newParents );
BmInferer_node_reinitWith= core.BmInferer_node_reinitWith
BmInferer_node_reinitWith.restype= c_void_p
BmInferer_node_reinitWith.argtypes= [c_void_p, c_digit, c_void_p]

# BmCondition* BmInferer_node_reinitWith_withDefault( BmInferer* self, digit index, BmCode* newDependenceList, BmBench* newDefaultDistrib );
BmInferer_node_reinitWith_withDefault= core.BmInferer_node_reinitWith_withDefault
BmInferer_node_reinitWith_withDefault.restype= c_void_p
BmInferer_node_reinitWith_withDefault.argtypes= [c_void_p, c_digit, c_void_p, c_void_p]

# BmBench* BmInferer_process( BmInferer* self, BmBench* inputDistribution );
BmInferer_process= core.BmInferer_process
BmInferer_process.restype= c_void_p
BmInferer_process.argtypes= [c_void_p, c_void_p]

# BmBench* BmInferer_process_newOverallDistribution( BmInferer* self, BmBench* inputDistribution );
BmInferer_process_newOverallDistribution= core.BmInferer_process_newOverallDistribution
BmInferer_process_newOverallDistribution.restype= c_void_p
BmInferer_process_newOverallDistribution.argtypes= [c_void_p, c_void_p]

# BmBench* BmInferer_processState_Action( BmInferer* self, BmCode* state, BmCode* action );
BmInferer_processState_Action= core.BmInferer_processState_Action
BmInferer_processState_Action.restype= c_void_p
BmInferer_processState_Action.argtypes= [c_void_p, c_void_p, c_void_p]

# char* BmInferer_print( BmInferer* self, char* output );
BmInferer_print= core.BmInferer_print
BmInferer_print.restype= c_void_p
BmInferer_print.argtypes= [c_void_p, c_void_p]

# char* BmInferer_printStateActionSignature( BmInferer* self, char* output );
BmInferer_printStateActionSignature= core.BmInferer_printStateActionSignature
BmInferer_printStateActionSignature.restype= c_void_p
BmInferer_printStateActionSignature.argtypes= [c_void_p, c_void_p]

# char* BmInferer_printDependency( BmInferer* self, char* output );
BmInferer_printDependency= core.BmInferer_printDependency
BmInferer_printDependency.restype= c_void_p
BmInferer_printDependency.argtypes= [c_void_p, c_void_p]

# BmEvaluator* newBmEvaluatorBasic( digit spaceDimention, digit numberOfCriteria );
newBmEvaluatorBasic= core.newBmEvaluatorBasic
newBmEvaluatorBasic.restype= c_void_p
newBmEvaluatorBasic.argtypes= [c_digit, c_digit]

# BmEvaluator* newBmEvaluatorWith( BmCode* newSpace, digit numberOfCriteria );
newBmEvaluatorWith= core.newBmEvaluatorWith
newBmEvaluatorWith.restype= c_void_p
newBmEvaluatorWith.argtypes= [c_void_p, c_digit]

# BmEvaluator* BmEvaluator_createWith( BmEvaluator* self, BmCode* newSpace, digit numberOfCriteria );
BmEvaluator_createWith= core.BmEvaluator_createWith
BmEvaluator_createWith.restype= c_void_p
BmEvaluator_createWith.argtypes= [c_void_p, c_void_p, c_digit]

# void deleteBmEvaluator( BmEvaluator* self );
deleteBmEvaluator= core.deleteBmEvaluator
deleteBmEvaluator.restype= c_void_p
deleteBmEvaluator.argtypes= [c_void_p]

# BmEvaluator* BmEvaluator_destroy( BmEvaluator* self );
BmEvaluator_destroy= core.BmEvaluator_destroy
BmEvaluator_destroy.restype= c_void_p
BmEvaluator_destroy.argtypes= [c_void_p]

# BmCode* BmEvaluator_space( BmEvaluator* self );
BmEvaluator_space= core.BmEvaluator_space
BmEvaluator_space.restype= c_void_p
BmEvaluator_space.argtypes= [c_void_p]

# digit BmEvaluator_numberOfCriteria( BmEvaluator* self );
BmEvaluator_numberOfCriteria= core.BmEvaluator_numberOfCriteria
BmEvaluator_numberOfCriteria.restype= c_digit
BmEvaluator_numberOfCriteria.argtypes= [c_void_p]

# BmValueFct* BmEvaluator_criterion( BmEvaluator* self, digit iCritirion );
BmEvaluator_criterion= core.BmEvaluator_criterion
BmEvaluator_criterion.restype= c_void_p
BmEvaluator_criterion.argtypes= [c_void_p, c_digit]

# BmVector* BmEvaluator_weights( BmEvaluator* self );
BmEvaluator_weights= core.BmEvaluator_weights
BmEvaluator_weights.restype= c_void_p
BmEvaluator_weights.argtypes= [c_void_p]

# double BmEvaluator_criterion_weight( BmEvaluator* self, digit iCritirion );
BmEvaluator_criterion_weight= core.BmEvaluator_criterion_weight
BmEvaluator_criterion_weight.restype= c_double
BmEvaluator_criterion_weight.argtypes= [c_void_p, c_digit]

# BmCode* BmEvaluator_criterion_mask( BmEvaluator* self, digit iCritirion );
BmEvaluator_criterion_mask= core.BmEvaluator_criterion_mask
BmEvaluator_criterion_mask.restype= c_void_p
BmEvaluator_criterion_mask.argtypes= [c_void_p, c_digit]

# double BmEvaluator_process( BmEvaluator* self, BmCode* input );
BmEvaluator_process= core.BmEvaluator_process
BmEvaluator_process.restype= c_double
BmEvaluator_process.argtypes= [c_void_p, c_void_p]

# double BmEvaluator_criterion_process( BmEvaluator* self, digit iCriterion, BmCode* input );
BmEvaluator_criterion_process= core.BmEvaluator_criterion_process
BmEvaluator_criterion_process.restype= c_double
BmEvaluator_criterion_process.argtypes= [c_void_p, c_digit, c_void_p]

# double BmEvaluator_processState_action( BmEvaluator* self, BmCode* state, BmCode* action );
BmEvaluator_processState_action= core.BmEvaluator_processState_action
BmEvaluator_processState_action.restype= c_double
BmEvaluator_processState_action.argtypes= [c_void_p, c_void_p, c_void_p]

# double BmEvaluator_processState_action_state( BmEvaluator* self, BmCode* state, BmCode* action, BmCode* statePrime );
BmEvaluator_processState_action_state= core.BmEvaluator_processState_action_state
BmEvaluator_processState_action_state.restype= c_double
BmEvaluator_processState_action_state.argtypes= [c_void_p, c_void_p, c_void_p, c_void_p]

# BmEvaluator* BmEvaluator_reinitCriterion( BmEvaluator* self, digit numberOfCriterion );
BmEvaluator_reinitCriterion= core.BmEvaluator_reinitCriterion
BmEvaluator_reinitCriterion.restype= c_void_p
BmEvaluator_reinitCriterion.argtypes= [c_void_p, c_digit]

# BmValueFct* BmEvaluator_criterion_reinitWith( BmEvaluator* self, digit iCrit, BmCode* newDependenceMask, BmVector* newValues );
BmEvaluator_criterion_reinitWith= core.BmEvaluator_criterion_reinitWith
BmEvaluator_criterion_reinitWith.restype= c_void_p
BmEvaluator_criterion_reinitWith.argtypes= [c_void_p, c_digit, c_void_p, c_void_p]

# void BmEvaluator_criterion_from_set( BmEvaluator* self, digit index, BmCode* option, digit output );
BmEvaluator_criterion_from_set= core.BmEvaluator_criterion_from_set
BmEvaluator_criterion_from_set.restype= c_void_p
BmEvaluator_criterion_from_set.argtypes= [c_void_p, c_digit, c_void_p, c_digit]

# void BmEvaluator_criterion_setWeight( BmEvaluator* self, digit iCritirion, double weight );
BmEvaluator_criterion_setWeight= core.BmEvaluator_criterion_setWeight
BmEvaluator_criterion_setWeight.restype= c_void_p
BmEvaluator_criterion_setWeight.argtypes= [c_void_p, c_digit, c_double]
