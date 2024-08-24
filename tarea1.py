meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "GG": "Good game (Buena partida)",
            "AFK": "Away from keyboard (Lejos del teclado)",
            "BTW": "By the way (Por cierto)",
            "CLICKBAIT": "Contenido diseñado para atraer clics de manera engañosa.",
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ").upper()
if word in meme_dict.keys():
    print(meme_dict[word])
    
else:
    print("Esta palabra no esta en el diccionario")
   
