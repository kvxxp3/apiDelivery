from flask import jsonify, Flask
from flask_mysqldb import MySQL
from flask_cors import CORS
from connection import config

#cambiar hostName por UbuntuServer al estar en red Karla
hostName = "CasaAgs"
serverPort = 5000

app = Flask(__name__)
CORS(app)
conexion = MySQL(app)

###########################################################################################
##################################    REQUEST METHODS    ##################################
###########################################################################################

###################### CLIENTES
# LISTA TODOS LOS CLIENTES
@app.route('/clientes', methods=['GET'])
def listar_clientes():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM cliente"
        cursor.execute(sql)
        datos = cursor.fetchall()
        data=[]
        for fila in datos:
            dato={'id':fila[0],'name':fila[1],'app':fila[2],'apm':fila[3],'number':fila[4],'user':fila[5],
                  'card':fila[5]}
            data.append(dato)
            
        datosJSON = jsonify(data)
        print(data)
        
        return datosJSON    
    except Exception as ex:
        return jsonify({'mensaje':"Error: "+ex})
    
#UN CLIENTE POR ID
@app.route('/clientes/<i>', methods=['GET'])
def clienteID(i):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM cliente WHERE idCliente='{0}'".format(i)
        cursor.execute(sql)
        datos = cursor.fetchone()
        
        if datos != None:
            dato={'id':datos[0],'name':datos[1],'app':datos[2],'apm':datos[3],'number':datos[4],'user':datos[5],
                  'card':datos[5]}
        else:
            dato={'id':'NULL','name':'NULL','app':'NULL','apm':'NULL','number':'NULL','user':'NULL',
                  'card':'NULL'}
            
        datosJSON = jsonify(dato)
        print(dato)
        
        return datosJSON    
    except Exception as ex:
        return jsonify({'mensaje':"Error: "+ex})

###################### DETALLES_PEDIDO
@app.route('/detalles_pedidos', methods=['GET'])
def listar_detalles_pedidos():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM detalles_pedido"
        cursor.execute(sql)
        datos = cursor.fetchall()
        data=[]
        for fila in datos:
            dato={'id':fila[0],'cantidad':fila[1],'precio':fila[2],'pedido':fila[3],'producto':fila[4]}
            data.append(dato)
            
        datosJSON = jsonify(data)
        print(data)
        
        return datosJSON    
    except Exception as ex:
        return jsonify({'mensaje':"Error: "+ex})

###################### DIRECCIONES
@app.route('/direcciones', methods=['GET'])
def listar_direcciones():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM direccion"
        cursor.execute(sql)
        datos = cursor.fetchall()
        data=[]
        for fila in datos:
            dato={'id':fila[0],'calle':fila[1],'colonia':fila[2],'numero':fila[3],'referencia':fila[4]}
            data.append(dato)
            
        datosJSON = jsonify(data)
        print(data)
        
        return datosJSON    
    except Exception as ex:
        return jsonify({'mensaje':"Error: "+ex})
    
###################### PEDIDOS
@app.route('/pedidos', methods=['GET'])
def listar_pedidos():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM pedido"
        cursor.execute(sql)
        datos = cursor.fetchall()
        data=[]
        for fila in datos:
            dato={'id':fila[0],'status':fila[1],'costo':fila[2],'fecha':fila[3],'hora':fila[4],'resena':fila[5],
                  'dir':fila[6],'cliente':fila[7]}
            data.append(dato)
            
        datosJSON = jsonify(data)
        print(data)
        
        return datosJSON    
    except Exception as ex:
        return jsonify({'mensaje':"Error: "+ex})
    
###################### PRODUCTOS
#TODOS LOS PRODUCTOS
@app.route('/productos', methods=['GET'])
def listar_productos():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM producto"
        cursor.execute(sql)
        datos = cursor.fetchall()
        data=[]
        for fila in datos:
            dato={'id':fila[0],'nombre':fila[1],'des':fila[2],'precio':fila[3],'restaurante':fila[4]}
            data.append(dato)
            
        datosJSON = jsonify(data)
        print(data)
        
        return datosJSON    
    except Exception as ex:
        return jsonify({'mensaje':"Error: "+ex})
    
#UN PRODUCTO POR ID
@app.route('/productos/<i>', methods=['GET'])
def productoID(i):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM producto WHERE idProducto='{0}'".format(i)
        cursor.execute(sql)
        datos = cursor.fetchone()
        
        if datos != None:
            dato={'id':datos[0],'nombre':datos[1],'des':datos[2],'precio':datos[3],'restaurante':datos[4]}
        else:
            dato={'id':'NULL','nombre':'NULL','des':'NULL','precio':'NULL','restaurante':'NULL'}
            
        datosJSON = jsonify(dato)
        print(dato)
        
        return datosJSON    
    except Exception as ex:
        return jsonify({'mensaje':"Error: "+ex})
    
###################### RESTAURANTES
# TODOS LOS RESTAURANTES
@app.route('/restaurantes', methods=['GET'])
def listar_restaurantes():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM restaurante"
        cursor.execute(sql)
        datos = cursor.fetchall()
        data=[]
        for fila in datos:
            dato={'id':fila[0],'name':fila[1],'number':fila[2],'branch':fila[3],'user':fila[4],'dir':fila[5],
                  'card':fila[5]}
            data.append(dato)
            
        datosJSON = jsonify(data)
        print(data)
        
        return datosJSON    
    except Exception as ex:
        return jsonify({'mensaje':"Error: "+ex})
    
#UN RESTAURANTE POR ID
@app.route('/restaurantes/<i>', methods=['GET'])
def restauranteID(i):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM restaurante WHERE idRestaurante='{0}'".format(i)
        cursor.execute(sql)
        datos = cursor.fetchone()
        
        if datos != None:
            dato={'id':datos[0],'name':datos[1],'number':datos[2],'branch':datos[3],'user':datos[4],'dir':datos[5],
                  'card':datos[5]}
        else:
            dato={'id':'NULL','name':'NULL','number':'NULL','branch':'NULL','user':'NULL','dir':'NULL',
                  'card':'NULL'}
            
        datosJSON = jsonify(dato)
        print(dato)
        
        return datosJSON    
    except Exception as ex:
        return jsonify({'mensaje':"Error: "+ex})
    
###################### TARJETAS
@app.route('/tarjetas', methods=['GET'])
def listar_tarjetas():
    try:
        #print('SIRVE')
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM tarjeta"
        cursor.execute(sql)
        datos = cursor.fetchall()
        data=[]
        for fila in datos:
            dato={'id':fila[0],'tipo':fila[1],'clabe':fila[2]}
            data.append(dato)
            
        datosJSON = jsonify(data)
        print(data)
        
        return datosJSON 
        #return jsonify({'mensaje':"Sirve."})
    except Exception as ex:
        return jsonify({'mensaje':"Error: "+ex})

###################### USUARIOS 
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM usuario"
        cursor.execute(sql)
        datos = cursor.fetchall()
        data=[]
        for fila in datos:
            usuario={'id':fila[0],'name':fila[1],'psw':fila[2],'email':fila[3],'user':fila[4]}
            data.append(usuario)
            
        datosJSON = jsonify(data)
        print(data)
        
        return datosJSON    
    except Exception as ex:
        return jsonify({'mensaje':"Error: "+ex})

###########################################################################################
##################################                       ##################################
###########################################################################################

    
def non_exist(e):
    return "<h1>La pagina no existe.</h1>"

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, non_exist)
    app.run(host=hostName, port=serverPort)