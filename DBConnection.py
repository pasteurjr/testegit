# -*- coding: utf-8 -*-

import mysql.connector

import configbd 






class DBConnection:
    __connection = None
    def __init__(self):
        print("Iniciando")
    @classmethod
    def Instancia(self):
        print("Dentro Instancia")
        if self.__connection == None:
            print("Iniciando a instancia unica")
            self.__connection = mysql.connector.connect(host=configbd.HOST,
                             user=configbd.USER,
                             password=configbd.PASSWORD,
                             port = configbd.PORT,
                             db=configbd.DB)
            self.__connection.set_charset_collation('latin1', 'latin1_general_ci')
        return self.__connection


