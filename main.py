import pandas as pd
import getpass


#--------------------------------USER CONFIGURATION--------------------------------
user = getpass.getuser()

file='24_07_23.xlsx'
if user == 'PC HOME':
    file_path = fr'C:\Users\PC HOME\OneDrive\Escritorio\{file}'
else:
    file_path = fr'Z:\1. Coordinadores\Asignaciones\Naturgy\Bases\Nuevas asignaciones\{file}'
#-------------------------------/USER CONFIGURATION--------------------------------

#Rutina principal
def main():

    df = pd.read_excel(file_path)
    for index, column in enumerate(df.columns):
        print(index, column)

    row = list(df['CTA CONTR'].drop_duplicates())
    print('')

    

if __name__ == '__main__':
    main()