user_inputs = {}

#3.1a
user_inputs[0]= {
        'objective': 'max',
        'c_coeff': [4,5] ,
        'coef_constraints': [
            [2,2],
            [1,0],
            [0,1],            
        ],
        'inequality_constraints': [
            '<=','<=','<='
        ],
        'b_value': [9,4,3],
        
        
        'coef_inequality_constraints':[
            [1,0],
            [0,1],
           
        ],
        
        'inequality_inequality_constraints':[
            '>=', '>='
        ],
    }

#3.1b
user_inputs[1]= {
        'objective': 'min',
        'c_coeff': [-2,-1] ,
        'coef_constraints': [
            [3,1],      
        ],
        'inequality_constraints': [
            '<='
        ],
        'b_value': [3],
        
        
        'coef_inequality_constraints':[
            [1,0],
            [0,1],
           
        ],
        
        'inequality_inequality_constraints':[
            '>=', '>='
        ],
    }
#3.1c
user_inputs[2]= {
        'objective': 'max',
        'c_coeff': [3,5] ,
        'coef_constraints': [
            [1,2],
            [1,0], 
            [0,1],
        ],
        'inequality_constraints': [
            '<=','<=','<='
        ],
        'b_value': [5,3,2],
        
        
        'coef_inequality_constraints':[
            [1,0],
            [0,1],
           
        ],
        
        'inequality_inequality_constraints':[
            '>=', '>='
        ],
    }
#3.4
user_inputs[3]= {
        'objective': 'min',
        'c_coeff': [-10, 57, 9, 24] ,
        'coef_constraints': [
            [.5, -5.5, -2.5, 9],
        [.5, -1.5, -.5, 1],
        [1, 0, 0, 0]
        ],
        'inequality_constraints': [
            '<=','<=','<='
        ],
        'b_value': [0, 0, 1],
        
        
        'coef_inequality_constraints':[
            [1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [0,0,0,1],
        ],
        
        'inequality_inequality_constraints':[
            '>=', '>=','>=','>='
        ],
    }
#3.6
user_inputs[4]= {
        'objective': 'min',
        'c_coeff': [2,-3,4] ,
        'coef_constraints': [
        [0,-2,-3],
        [1,1,2],
        [1,2,3]
        ],
        'inequality_constraints': [
            '>=','<=','<='
        ],
        'b_value': [-5,4,7],
        
        
        'coef_inequality_constraints':[
            [1,0,0],
            [0,1,0],
            [0,0,1],
        ],
        
        'inequality_inequality_constraints':[
            '>=', '>=','>='
        ],
    }
#3.14a
user_inputs[5]= {
        'objective': 'max',
        'c_coeff': [1,3,-1] ,
        'coef_constraints': [
            [2,2,-1],
            [3,-2,1],
            [1,-3,1]
        ],
        'inequality_constraints': [
            '<=','<=','<='
        ],
        'b_value': [10,10,10],
        
        
        'coef_inequality_constraints':[
            [1,0,0],
            [0,1,0],
            [0,0,1],
        ],
        
        'inequality_inequality_constraints':[
            '>=', '>=','>='
        ],
    }
#3.14f
user_inputs[6]= {
        'objective': 'min',
        'c_coeff': [2,-5] ,
        'coef_constraints': [
            [1,3],
            [2,-3],
            [-1,1],
            [-1,2],
            
        ],
        'inequality_constraints': [
            '<=','<=','<=','<='
        ],
        'b_value': [10,0,3,1],
        
        
        'coef_inequality_constraints':[
            [1,0],
            [0,1],
           
        ],
        
        'inequality_inequality_constraints':[
            'None', 'None'
        ],
        
    }

#3.14g
user_inputs[7]= {
        'objective': 'min',
        'c_coeff': [-4,-5] ,
        'coef_constraints': [
            [1,2],
            [1,-1],
            [2,1],
            [3,4],
            
        ],
        'inequality_constraints': [
            '<=','<=','<=','<='
        ],
        'b_value': [3,2,3,8],
        
        
        'coef_inequality_constraints':[
            [1,0],
            [0,1],
           
        ],
        
        'inequality_inequality_constraints':[
            '>=', 'None'
        ],
        
    }

#3.15
user_inputs[2]= {
        'objective': 'max',
        'c_coeff': [3,1,0] ,
        'coef_constraints': [
            [1,2,0],
            [1,1,-1],
            [7,3,-5],            
        ],
        'inequality_constraints': [
            '<=','<=','<='
        ],
        'b_value': [5,2,20],
        
        
        'coef_inequality_constraints':[
            [1,0,0],
            [0,1,0],
            [0,0,1]
        ],
        
        'inequality_inequality_constraints':[
            '>=', '>=','>='
        ],
        
    }

#2.6a
user_inputs[8]= {
        'objective': 'max',
        'c_coeff': [2,-6,0] ,
        'coef_constraints': [
            [-1,-1,-1],
            [2,-1,1],
        ],
        'inequality_constraints': [
            '<=','<='
        ],
        'b_value': [-2,1],
        
        
        'coef_inequality_constraints':[
            [1,0,0],
            [0,1,0],
            [0,0,1]
        ],
        
        'inequality_inequality_constraints':[
            '>=', '>=','>='
        ],
        
    }

#2.6b
user_inputs[9]= {
        'objective': 'min',
        'c_coeff': [-1,-3] ,
        'coef_constraints': [
            [1,1],
            [-1,1],
            [1,2],
        ],
        'inequality_constraints': [
            '>=','<=','<='
        ],
        'b_value': [3,-1,4],
        
        
        'coef_inequality_constraints':[
            [1,0],
            [0,1],
        ],
        
        'inequality_inequality_constraints':[
            '>=', '>='
        ],
        
    }

#2.6c
user_inputs[10]= {
        'objective': 'max',
        'c_coeff': [1,3] ,
        'coef_constraints': [
            [-1,-1],
            [-1,1],
            [-1,2],
        ],
        'inequality_constraints': [
            '<=','<=','<='
        ],
        'b_value': [-3,-1,2],
        
        
        'coef_inequality_constraints':[
            [1,0],
            [0,1],
        ],
        
        'inequality_inequality_constraints':[
            '>=', '>='
        ],
        
    }

#2.9a
user_inputs[11]= {
        'objective': 'max',
        'c_coeff': [-1,-3,-1] ,
        'coef_constraints': [
            [2,-5,1],
            [2,-1,2],
        ],
        'inequality_constraints': [
            '<=','<='
        ],
        'b_value': [-5,-4],
        
        
        'coef_inequality_constraints':[
            [1,0,0],
            [0,1,0],
            [0,0,1],

        ],
        
        'inequality_inequality_constraints':[
            '>=', '>=','>='
        ],
        
    }


#2.15
user_inputs[12]= {
        'objective': 'max',
        'c_coeff': [1,-1] ,
        'coef_constraints': [
            [-2,1],
            [-1,-2],
        ],
        'inequality_constraints': [
            '<=','<='
        ],
        'b_value': [-1,-2],
        
        
        'coef_inequality_constraints':[
            [1,0],
            [0,1],

        ],
        
        'inequality_inequality_constraints':[
            '>=', '>='
        ],
        
    }

user_inputs[13]= {'objective': 'max', 
                  'c_coeff': [1.0, 2.0, 33.0, 3.0, 3.0], 
 'coef_constraints': [[3.0, 3.0, 3.0, 3.0, 3.0], 
                      [3.0, 1.0, 1.0, 1.0, 1.0], 
                      [1.0, 1.0, 1.0, 1.0, 1.0], 
                      [1.0, 3.0, 3.0, 3.0, 3.0], 
                      [2.0, 3.0, 3.0, 3.0, 33.0]], 
 'inequality_constraints': ['<=', '<=', '=', '<=', '>='], 
 'b_value': [2.0, 2.0, -2.0, -1.0, -10.0], 
 'coef_inequality_constraints': ([
    [1., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0.],
       [0., 0., 1., 0., 0.],
       [0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 1.]]), 
 'inequality_inequality_constraints': ['>=', 'None', 'None', '>=', '<='], 
}


#3.14g
user_inputs[14]= {
        'objective': 'min',
        'c_coeff': [-4,-5] ,
        'coef_constraints': [
            [1,2],
            [1,-1],
            [2,1],  
            [3,4],          
        ],
        'inequality_constraints': [
            '<=','<=','<=','<='
        ],
        'b_value': [3,2,3,8],
        
        
        'coef_inequality_constraints':[
            [1,0],
            [0,1]
        ],
        
        'inequality_inequality_constraints':[
            '>=', 'None'
        ],
        
    }


#1.17
user_inputs[15]= {
        'objective': 'max',
        'c_coeff': [1,3,2] ,
        'coef_constraints': [
            [1,1,1],
            [7,2,3],
            [1,5,4],  
        ],
        'inequality_constraints': [
            '=','<=','<='
        ],
        'b_value': [1,20,30],
        
        
        'coef_inequality_constraints':[
            [1,0,0],
            [0,1,0],
            [0,0,1]
        ],
        
        'inequality_inequality_constraints':[
            '>=', '>=','>='
        ],
        
    }


#1.10a
user_inputs[16]= {
        'objective': 'min',
        'c_coeff': [-1,1] ,
        'coef_constraints': [
            [-1,-2],
            [1,-2],
            [-1,1],  
        ],
        'inequality_constraints': [
            '<=','<=','<='
        ],
        'b_value': [6,4,1],
        
        
        'coef_inequality_constraints':[
            [1,0],
            [0,1],
            
        ],
        
        'inequality_inequality_constraints':[
            '<=', '<='
        ],
        
    }




#1.17a
user_inputs[17]= {
        'objective': 'max',
        'c_coeff': [1,3,2] ,
        'coef_constraints': [
            [1,1,1],
            [7,2,3],
            [1,5,4],  
        ],
        'inequality_constraints': [
            '=','<=','<='
        ],
        'b_value': [1,20,30],
        
        
        'coef_inequality_constraints':[
            [1,0,0],
            [0,1,0],
            [0,0,1],
        ],
        
        'inequality_inequality_constraints':[
            '>=', '>=','>='
        ],
        
    }