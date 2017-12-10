	# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 23:18:13 2017

@author: Rods Freitas
"""

import xlsxwriter
import helper

filtro = {'python','javascript','ux','html'}

workbook = xlsxwriter.Workbook('data_twitter.xlsx')
worksheet = workbook.add_worksheet()

data = helper.getData(filtro)

worksheet.write(0,0,'Linguagens')
worksheet.write(0,1,'Quantidade')

row = 1
col = 0

for item,number in data:
	worksheet.write(row,col,item)
	worksheet.write(row,col + 1, helper.getQuantidade(number))
	row+=1

worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B2:B5)')

workbook.close()