#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Módulo encargado de realizar las operaciones a la base de datos MariaDB
"""

# Datos de conexión a la base de datos
BD = {
    "database":"BeduTravels",
    "host":"localhost",
    "user":"BeduTravels",
    "password":"BeduTravels"
}

# zona de imports
from mysql.connector import connect, Error


def conecta_bd():
    """
    Se conecta a la base de datos BD, regresa un conecto o None en caso
    de error.
    """
    try:
        conn = connect(**BD)
    except Error as err:
        print(err)
        return None

    return conn

def obtiene_registros(tabla):
    """
    Obtiene la lista de registros de tabla y los regresa en forma de lista
    """
    # Se realiza la conexión a la base de datos
    conn = conecta_bd()
    if conn:
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()
        # Se crea la consulta SQL
        sql = "SELECT * FROM {}".format(tabla)
        # Se ejecuta la consulta
        cur.execute(sql)
        # Se obtiene la lista de campos y se agrega como primer posición en la
        # lista de resultados.
        registros = [[r[0].capitalize() for r in cur.description]]
        # Se obtiene la lista de resultados de la consulta SQL
        registros += cur.fetchall()
        # Se cierra la BD
        conn.close()

        return registros
    else:
        # Si no hay conexión a la BD regresamos una lista vacía
        return []

def obtiene_tablas():
    """
    Obtiene la lista de tablas en la base de datos
    """
    # Se realiza la conexión a la base de datos
    conn = conecta_bd()
    if conn:
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()
        # Se crea la consulta SQL
        sql = "SHOW TABLES"
        # Se ejecuta la consulta
        cur.execute(sql)
        # Se obtiene la lista de resultados de la consulta SQL
        registros = cur.fetchall()
        # Se cierra la BD
        conn.close()

        return registros
    else:
        # Si no hay conexión a la BD regresamos una lista vacía
        return []

def ejecuta_sql(sql):
    """
    Ejecuta las instrucciones proporcionadas por sql y regresa True en
    caso de éxtio, False en caso contrario.
    """
    # Se realiza la conexión a la base de datos
    conn = conecta_bd()
    if conn:
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()
        # Se ejecuta la consulta
        cur.execute(sql)
        # Se cierra la BD
        conn.close()

        return True
    else:
        # Si no hay conexión a la BD regresamos una lista vacía
        return False

def agrega_registro(tabla, valores):
    """ Agrega un registro en tabla """
    # Se realiza la conexión a la BD
    conn = conecta_bd()
    if conn:
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()
        # Se arma una tupla con los valores de los campos
        # Se crea una cadena con tantos símbolos "%s" como valores
        # tengamos separados por comas
        signos = ", ".join(["%s"] * len(valores))
        # Se crea la consulta en SQL
        sql = "insert into {} values (null, {})".format(tabla, signos)
        # Se ejecuta la consulta
        cur.execute(sql, valores)
        # Se ejecuta un commit para indicar que la inserción se ejecute como una
        # operación atómica.
        conn.commit()
        # Se cierra la BD
        conn.close()
        # Se regresa True para indicar que el registro se ha insertado con
        # éxito
        return True

    return False  # En caso de error

def obtiene_viajes():
    """
    Obtiene la lista de viajes registrados y los regresa en forma de lista
    """
    # Sugerencia: Esta función no necesita hacer uso de la conexión a la
    # base de datos de forma directa, puedes hacer uso de las funciones
    # ya creada para obtener los registros necesarios e ir armando los
    # registros de los viajes solicitados.
    pass

    return []
