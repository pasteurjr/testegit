#app.py

from flask import Flask, request,Response #import main Flask class and request object
import jsonpickle
app = Flask(__name__) #create the Flask app


from flask import jsonify
import mysql.connector

import atexit

#import pymysql 




import configbd

#from DBConnection import DBConnection   
from flask.json import JSONEncoder
from datetime import date
  

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, date):
                return obj.isoformat()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)       
app.json_encoder = CustomJSONEncoder
#connection = DBConnection.Instancia()

def retornatudocliente(cliente):
    
    connection = mysql.connector.connect(host=configbd.HOST,
                             user=configbd.USER,
                             password=configbd.PASSWORD,
                             port = configbd.PORT,
                             db=configbd.DB)
                          #   charset='utf8mb4',
                            # cursorclass=mysql.connector.cursors.DictCursor)
    
     
    
    #connection = DBConnection.Instancia()
    
    try:
        

        print(connection)
        cursor = connection.cursor(dictionary=True, buffered=True)
        sql = "Select * from Cliente where idCliente = %s"
        cursor.execute(sql,(cliente,))
        result = cursor.fetchone()
        print(result)

        cursor.close()
        #connection.close()
        return result
    except mysql.connector.Error as err:
        #print(mysql.connector.Error.errno)
         
        print("Erro: {}".format(err))
        return "Erro: {}".format(err)        
    finally:
        connection.close()
   
def retornalayoutestab(estabelecimento):
    
    connection = mysql.connector.connect(host=configbd.HOST,
                             user=configbd.USER,
                             password=configbd.PASSWORD,
                             port = configbd.PORT,
                             db=configbd.DB)
                          #   charset='utf8mb4',
                            # cursorclass=mysql.connector.cursors.DictCursor)
    
     
    
    #connection = DBConnection.Instancia()
    
    try:
        

        print(connection)
        cursor = connection.cursor(dictionary=True, buffered=True)
        sql = ("SELECT numEstabelecimento, primaryColor,primaryFontColor, secondaryColor,secondaryFontColor,"
        " menu1,menu2,menu3,menu4,menu5,labelFidelidade,labelPromocoes,labelAgenda,labelCatalogo,"
        "labelPesquisaSatisfacao, labelSobre,labelComoChegar,labelComprasOnline,labelIndiqueAmigo,"
        "labelEstacionamento,tipoEstabelecimento "
        " FROM WebAppLayout WHERE numEstabelecimento = %s")
        cursor.execute(sql,(estabelecimento,))
        result = cursor.fetchone()
        print(result)

        cursor.close()
        #connection.close()
        return result
    except mysql.connector.Error as err:
        #print(mysql.connector.Error.errno)
         
        print("Erro: {}".format(err))
        return "Erro: {}".format(err)        
    finally:
        connection.close()  



def retornaunidadeestaburl(extensaourl):
    
    connection = mysql.connector.connect(host=configbd.HOST,
                             user=configbd.USER,
                             password=configbd.PASSWORD,
                             port = configbd.PORT,
                             db=configbd.DB)
                          #   charset='utf8mb4',
                            # cursorclass=mysql.connector.cursors.DictCursor)
    
     
    
    #connection = DBConnection.Instancia()
    
    try:
        

        print(connection)
        cursor = connection.cursor(dictionary=True, buffered=True)
        sql = ("SELECT nomeEstabelecimento,senha,cnpj,contato,Estabelecimento.telefone, Estabelecimento.emailContato,"
               "Unidade.numUnidade,Unidade.nomeUnidade,Unidade.labelUnidade,Unidade.emailUnidade,Unidade.telefone,"
               "Unidade.endereco,Unidade.latitude,Unidade.longitude FROM Unidade INNER JOIN Estabelecimento"
               " ON  (Estabelecimento.numEstabelecimento = Unidade.numEstabelecimento) WHERE extensaoUrl=%s ORDER BY numunidade")
        cursor.execute(sql,(extensaourl,))
        result = cursor.fetchall()
        print(result)

        cursor.close()
        #connection.close()
        return result
    except mysql.connector.Error as err:
        #print(mysql.connector.Error.errno)
         
        print("Erro: {}".format(err))
        return "Erro: {}".format(err)        
    finally:
        connection.close()




def retornaimagemlayoutestab(estabelecimento,campo):
    
    connection = mysql.connector.connect(host=configbd.HOST,
                             user=configbd.USER,
                             password=configbd.PASSWORD,
                             port = configbd.PORT,
                             db=configbd.DB)
                          #   charset='utf8mb4',
                            # cursorclass=mysql.connector.cursors.DictCursor)
    
     
    
    #connection = DBConnection.Instancia()
    
    try:
        

        print(connection)
        #cursor = connection.cursor(dictionary=True, buffered=True)        
        cursor = connection.cursor()
        sql = "SELECT "+campo+" FROM WebAppLayout WHERE numEstabelecimento = %s"
        cursor.execute(sql,(estabelecimento,))
        result = cursor.fetchone()
        #print(result)
        #for row in result:
        #    image = row[0]
       
        cursor.close()
        #connection.close()
        return result
    except mysql.connector.Error as err:
        #print(mysql.connector.Error.errno)
         
        print("Erro: {}".format(err))
        return "Erro: {}".format(err)        
    finally:
        connection.close()  




def close_connection():
    
    print(connection)
    connection.close()
    
    print("Conexão com banco fechada")
    
    

@app.route('/retorna_tudo_cliente')
def retorna_tudo_cliente():
    cli = request.args.get('idcliente')
    
    cliente = retornatudocliente(cli)
    
    resp= jsonify(cliente)
    
    resp.status_code = 200
    return resp
    #return Response(response=estab, status=200, mimetype="application/json")

@app.route('/retorna_unidade_estab_url')
def retorna_unidade_estab_url():
    extensaourl = request.args.get('extensaourl')
    
    estab = retornaunidadeestaburl(extensaourl)
    
    resp= jsonify(estab)
    
    resp.status_code = 200
    return resp
    #return Response(response=estab, status=200, mimetype="application/json")


@app.route('/retorna_layout_estab')
def retorna_layout_estab():
    est = request.args.get('est')
    
    estab = retornalayoutestab(est)
    
    resp= jsonify(estab)
    
    resp.status_code = 200
    return resp
    #return Response(response=estab, status=200, mimetype="application/json")

@app.route('/retorna_imagem_layout_estab')
def retorna_imagem_layout_estab():
    est = request.args.get('est')
    campo = request.args.get('campo')
    icon = retornaimagemlayoutestab(est,campo)
    

    
    return Response(response=icon, status=200, mimetype="image/jpeg")







if __name__ == '__main__':
    #atexit.register(close_connection)
    
    app.config['JSON_AS_ASCII'] = False
    app.config['JSON_SORT_KEYS'] = False
    app.run(host="192.168.1.5",debug=True, port=5052) #run app in debug mode on port 5000