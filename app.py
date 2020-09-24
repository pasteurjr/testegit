#app.py

from flask import Flask, request,Response #import main Flask class and request object
import jsonpickle
app = Flask(__name__) #create the Flask app
#from kivy.clock import Clock
import pymysql.cursors
import pymysql
from flask import jsonify




import configbd




def retornanomecnpjestab(codigo):
    #atualiza o token do beacon após 3 registros distintos
    connection = pymysql.connect(host=configbd.HOST,
                             user=configbd.USER,
                             password=configbd.PASSWORD,
                             port = configbd.PORT,
                             db=configbd.DB,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    
    try:
        

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT nomeestabelecimento, cnpj FROM Estabelecimento WHERE numEstabelecimento = %s"
            cursor.execute(sql,(codigo))
            result = cursor.fetchone()
            print(result)
            return result["nomeestabelecimento"],result["cnpj"]
    except:
        
        return "ERRO",result        
    finally:
        connection.close()
    
def retornatodosestab():
    #atualiza o token do beacon após 3 registros distintos
    connection = pymysql.connect(host=configbd.HOST,
                             user=configbd.USER,
                             password=configbd.PASSWORD,
                             port = configbd.PORT,
                             db=configbd.DB,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    
    try:
        

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT nomeestabelecimento, cnpj FROM Estabelecimento"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
            return result
    except:
        
        return "ERRO"        
    finally:
        connection.close()    


@app.route('/retorna_todos_estab')
def retorna_todos_estab():
    
    
    #global tokenatu
    estab = retornatodosestab()
    

    resp= jsonify(estab)
    resp.status_code = 200
    return resp
    #return Response(response=resp, status=200, mimetype="application/json")




@app.route('/retorna_nome_cnpj_estab')
def retorna_nome_cnpj_estab():
    
    
    #global tokenatu
    nome,cnpj = retornanomecnpjestab(1)
    

    response_pickled= jsonpickle.encode({"nome":"{}".format(nome),"cnpj":"{}".format(cnpj)})
    return Response(response=response_pickled, status=200, mimetype="application/json")





if __name__ == '__main__':
    
    app.run(host="192.168.1.5",debug=True, port=5002) #run app in debug mode on port 5000