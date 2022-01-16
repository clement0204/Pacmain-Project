import cv2
import mediapipe as mp
import numpy as np
import os
import time
import random
from game.video_analysis.player_movements import *
import pandas as pd

cam = cv2.VideoCapture(0)
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

def measure_angle(data):

    if data[0] != None:
        x1 = data[0]["paume"][0]
        x2 = data[0]["paume"][1]
        y1 = data[0]["pinky1"][0]
        y2 = data[0]["pinky1"][1]
        z1 = data[0]["pinky4"][0]
        z2 = data[0]["pinky4"][1]

        a = (x1 - y1, x2 - y2)
        b = (y1 - z1, y2 - z2)

        moda = np.sqrt((x1-y1)**2+(x2-y2)**2)
        modb = np.sqrt((y1-z1)**2+(y2-z2)**2)
        scal = np.dot(a,b) 

        return int(np.arccos(scal/(moda*modb))*180/np.pi)

    else: 
        return None

    
k = 1
arr = np.array([[0,0]])

### Décommenter pour voir générer un fichier excel issu de l'acquisition de 
### la variation de l'angle de la main sur 20 frames

"""while True:
    k+=1

    data = collect_data_recording(mp_drawing,mp_drawing_styles,mp_hands,cam)

    image = cv2.cvtColor(data[1], cv2.COLOR_RGB2BGR)
    cv2.imshow('Camera', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break
    
    row = np.array([k,measure_angle(data)])
    arr = np.append(arr,[row],axis= 0)
    #print(initialization_measure(data))
    #print(data[0])
    #print(measure_angle(data))

    if k > 200:
        break


df = pd.DataFrame(arr)
#df.to_excel(excel_writer = "/Users/clementasseraf/Desktop/Pacmain/test.xlsx")


# Create a Pandas Excel writer using XlsxWriter as the engine.
excel_file = 'scatter_test.xlsx'
sheet_name = 'Sheet1'

writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
df.to_excel(writer, sheet_name=sheet_name)

# Access the XlsxWriter workbook and worksheet objects from the dataframe.
workbook = writer.book
worksheet = writer.sheets[sheet_name]

# Create a chart object.
chart = workbook.add_chart({'type': 'scatter'})

# Configure the series of the chart from the dataframe data.
max_row = len(df)

chart.add_series({
    'name':       'data',
    'categories': '=Sheet1!$B$1:$B$201',
    'values':     'Sheet1!$C$1:$C$201',
    'marker':     {'type': 'plus', 'size': 3},
    })

# Configure the chart axes.
chart.set_x_axis({'name': 'Frame'})
chart.set_y_axis({'name': 'Angle en degrés',
                  'major_gridlines': {'visible': False}})


# Insert the chart into the worksheet.
worksheet.insert_chart('K2', chart)

# Close the Pandas Excel writer and output the Excel file.
writer.save()
"""
