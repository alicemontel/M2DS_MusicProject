from pandas import DataFrame, read_csv
from datetime import datetime
import pandas as pd;
import csv;

        
# les reponses sur les musiques uniquement
with open("../../Source/responses.csv", "r") as fichier:
    cr = csv.reader(fichier,delimiter=";");
    rempli = True;
    
    with open("music.csv", "w") as denFile:
        fileWriter = csv.writer(denFile, delimiter=",")
        fileWriter.writerow(
            ["Music", "Slow songs or fast songs", "Dance", "Folk", "Country", "Classical music", "Musical", "Pop", "Rock", "Metal or Hardrock", "Punk", "Hiphop, Rap", "Reggae, Ska", "Swing, Jazz", "Rock n roll", "Alternative", "Latino", "Techno, Trance", "Opera"])
        compteur = 0
        for row in cr:
            ligne = row[0].split(',');
            
            i = 0;
            while i < 19:
                if(ligne[i] == ""):
                    rempli = False;
                i +=1
                
            if ( compteur > 0 and rempli):
                fileWriter.writerow([ligne[0], ligne[1], ligne[2], ligne[3], ligne[4], ligne[5], ligne[6], ligne[7], ligne[8], ligne[9],  ligne[10], ligne[11], ligne[12], ligne[13], ligne[14], ligne[15],ligne[16], ligne[17], ligne[18]])
            else:
                rempli = True;
            compteur = compteur + 1
            
        
# les reponses sur les musiques et les films
with open("../../Source/responses.csv", "r") as fichier:
    cr = csv.reader(fichier,delimiter=";");
    rempli = True;
    
    with open("music_movie.csv", "w") as denFile:
        fileWriter = csv.writer(denFile, delimiter=",")
        fileWriter.writerow(
            ["Music", "Slow songs or fast songs", "Dance", "Folk", "Country", "Classical music", "Musical", "Pop", "Rock", "Metal or Hardrock", "Punk", "Hiphop, Rap", "Reggae, Ska", "Swing, Jazz", "Rock n roll", "Alternative", "Latino", "Techno, Trance", "Opera", "Movies", "Horror", "Thriller", "Comedy", "Romantic", "Sci-fi", "War", "Fantasy/Fairy tales", "Animated", "Documentary", "Western", "Action"])
        compteur = 0
        for row in cr:
            ligne = row[0].split(',');
            
            i = 0;
            while i < 31:
                if(ligne[i] == ""):
                    rempli = False;
                i +=1
                
            if ( compteur > 0 and rempli):
                fileWriter.writerow([ligne[0], ligne[1], ligne[2], ligne[3], ligne[4], ligne[5], ligne[6], ligne[7], ligne[8], ligne[9],  ligne[10], ligne[11], ligne[12], ligne[13], ligne[14], ligne[15],ligne[16], ligne[17], ligne[18], ligne[19], ligne[20], ligne[21], ligne[22], ligne[23], ligne[24], ligne[25], ligne[26], ligne[27], ligne[28], ligne[29], ligne[30]])
            else:
                rempli = True;
            compteur = compteur + 1
            
            
# les reponses sur les musiques et les films
with open("../../Source/responses.csv", "r") as fichier:
    cr = csv.reader(fichier,delimiter=";");
    rempli = True;
    
    with open("movie.csv", "w") as denFile:
        fileWriter = csv.writer(denFile, delimiter=",")
        fileWriter.writerow(
            ["Movies", "Horror", "Thriller", "Comedy", "Romantic", "Sci-fi", "War", "Fantasy/Fairy tales", "Animated", "Documentary", "Western", "Action"])
        compteur = 0
        for row in cr:
            ligne = row[0].split(',');
            
            i = 0;
            for i in range( 19,31):
                if(ligne[i] == ""):
                    rempli = False;
                i +=1
                
            if ( compteur > 0 and rempli):
                fileWriter.writerow([ligne[19], ligne[20], ligne[21], ligne[22], ligne[23], ligne[24], ligne[25], ligne[26], ligne[27], ligne[28], ligne[29], ligne[30]])
            else:
                rempli = True;
            compteur = compteur + 1


