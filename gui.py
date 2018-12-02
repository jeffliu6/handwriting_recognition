import PySimpleGUI27 as sg 
import cv2 
import numpy as np
import preprocessor

if __name__ == "__main__":
    cv2.namedWindow("Live Video Capture")
    cap = cv2.VideoCapture(0)
    layout = [
            [sg.Text('Enter a filename...')],      
            [sg.Input(key='_PATH_'), sg.FileBrowse()],  
            [sg.Text('Result:'), sg.Text("", key='_RESULT_')],
            [sg.Text('Latex Code: '), sg.Text("", key='_LATEX_')],    
            [sg.OK(), sg.Exit()] ]
    window = sg.Window('Handwritting to Latex').Layout(layout)  

    while(True):
        event, values = window.Read()
        if event is None or event == "Exit":
            break 
        if values['_INPUT_']: 
            img = preprocessor.process_image(values['_INPUT_'])
            str_rep = classifier.classify(img)
            result = postprocessor.postProcess(str_rep) 
            if result: 
                window.Element('_RESULT_').Update(result[0])
                window.Element('_LATEX_').Update(result[1])

        
