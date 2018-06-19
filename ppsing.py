
from nltk import word_tokenize
import unicodedata 
import pickle


abc={'q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','ñ','m',' ','.'}#,'1','2','3','4','5','6','7','8','9'}

stop_words=['de', 'la', 'que', 'el', 'en', 'y', 'a', 'los', 'del', 'se', 'las', 'por', 'un', 'para', 'con', 'no', 'una', 'su', 'al', 'lo', 'como', 'mas', 'pero', 'sus', 'le', 'ya', 'o', 'este', 'si', 'porque', 'esta', 'entre', 'cuando', 'muy', 'sin', 'sobre', 'tambien', 'me', 'hasta', 'hay', 'donde', 'quien', 'desde', 'todo', 'nos', 'durante', 'todos', 'uno', 'les', 'ni', 'contra', 'otros', 'ese', 'eso', 'ante', 'ellos', 'e', 'esto', 'mi', 'antes', 'algunos', 'que', 'unos', 'yo', 'otro', 'otras', 'otra', 'el', 'tanto', 'esa', 'estos', 'mucho', 'quienes', 'nada', 'muchos', 'cual', 'poco', 'ella', 'estar', 'estas', 'algunas', 'algo', 'nosotros', 'mi', 'mis', 'tu', 'te', 'ti', 'tu', 'tus', 'ellas', 'nosotras', 'vosostros', 'vosostras', 'os', 'mio', 'mia', 'mios', 'mias', 'tuyo', 'tuya', 'tuyos', 'tuyas', 'suyo', 'suya', 'suyos', 'suyas', 'nuestro', 'nuestra', 'nuestros', 'nuestras', 'vuestro', 'vuestra', 'vuestros', 'vuestras', 'esos', 'esas', 'estoy', 'estas', 'esta', 'estamos', 'estais', 'estan', 'este', 'estes', 'estemos', 'esteis', 'esten', 'estare', 'estaras', 'estara', 'estaremos', 'estareis', 'estaran', 'estaria', 'estarias', 'estariamos', 'estariais', 'estarian', 'estaba', 'estabas', 'estabamos', 'estabais', 'estaban', 'estuve', 'estuviste', 'estuvo', 'estuvimos', 'estuvisteis', 'estuvieron', 'estuviera', 'estuvieras', 'estuvieramos', 'estuvierais', 'estuvieran', 'estuviese', 'estuvieses', 'estuviesemos', 'estuvieseis', 'estuviesen', 'estando', 'estado', 'estada', 'estados', 'estadas', 'estad', 'he', 'has', 'ha', 'hemos', 'habeis', 'han', 'haya', 'hayas', 'hayamos', 'hayais', 'hayan', 'habre', 'habras', 'habra', 'habremos', 'habreis', 'habran', 'habria', 'habrias', 'habriamos', 'habriais', 'habrian', 'habia', 'habias', 'habiamos', 'habiais', 'habian', 'hube', 'hubiste', 'hubo', 'hubimos', 'hubisteis', 'hubieron', 'hubiera', 'hubieras', 'hubieramos', 'hubierais', 'hubieran', 'hubiese', 'hubieses', 'hubiesemos', 'hubieseis', 'hubiesen', 'habiendo', 'habido', 'habida', 'habidos', 'habidas', 'soy', 'eres', 'es', 'somos', 'sois', 'son', 'sea', 'seas', 'seamos', 'seais', 'sean', 'sere', 'seras', 'sera', 'seremos', 'sereis', 'seran', 'seria', 'serias', 'seriamos', 'seriais', 'serian', 'era', 'eras', 'eramos', 'erais', 'eran', 'fui', 'fuiste', 'fue', 'fuimos', 'fuisteis', 'fueron', 'fuera', 'fueras', 'fueramos', 'fuerais', 'fueran', 'fuese', 'fueses', 'fuesemos', 'fueseis', 'fuesen', 'sintiendo', 'sentido', 'sentida', 'sentidos', 'sentidas', 'siente', 'sentid', 'tengo', 'tienes', 'tiene', 'tenemos', 'teneis', 'tienen', 'tenga', 'tengas', 'tengamos', 'tengais', 'tengan', 'tendre', 'tendras', 'tendra', 'tendremos', 'tendreis', 'tendran', 'tendria', 'tendrias', 'tendriamos', 'tendriais', 'tendrian', 'tenia', 'tenias', 'teniamos', 'teniais', 'tenian', 'tuve', 'tuviste', 'tuvo', 'tuvimos', 'tuvisteis', 'tuvieron', 'tuviera', 'tuvieras', 'tuvieramos', 'tuvierais', 'tuvieran', 'tuviese', 'tuvieses', 'tuviesemos', 'tuvieseis', 'tuviesen', 'teniendo', 'tenido', 'tenida', 'tenidos', 'tenidas', 'tened','asi','q','d']



#se carga el diccionario si no existe crea uno nuevo
name_dict='dic1'
frec_words=dict()
try:
    infile = open(name_dict,'rb')
    frec_words = pickle.load(infile)
    infile.close() 
except FileNotFoundError:
    frec_words=dict()

#esta funcion elmina todos los signos que no son palabras
def elimina_sign(text):
    text_out=''
    for i in text:
        if i not in abc:
             text_out+=' '
        else :
            text_out +=i
    return text_out

def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

## text es un string que deseas preprocesar, modificas el diccionario.
def processing(text):
    output=list()        
    
    #quita el enlace
    text=text.split('https')[0]

    #pasa todo a minusculas
    text = text.lower()

    #elmina signos de puntuacion
    text=elimina_tildes(text)

    #elimina caracteres
    text=elimina_sign(text)

    #separa el texto por frases u oraciones
    frases=text.split('.');

    #separa por las palabras
    for fr in frases:
        if len(fr)!=0: 
            words_sw = word_tokenize(fr)
            words=[]
            for i in words_sw:
                if (len(i)>1):
                    if (i not in stop_words):
                                           
                        words.append(i)
                    
                        if i not in frec_words.keys():
                            frec_words[i]=1;
                        else:
                            frec_words[i]=frec_words[i]+1
            if len(words)!=0:            
                output.append(words)

    return output

#mismo codigo para preporsseing esta version se corre cuando el modelo ya esta creado.
def ptext(text):
    output=list()        
    
    #quita el enlace
    text=text.split('https')[0]

    #pasa todo a minusculas
    text = text.lower()

    #elmina signos de puntuacion
    text=elimina_tildes(text)

    #elimina caracteres
    text=elimina_sign(text)

    #separa el texto por frases u oraciones
    frases=text.split('.');

    #separa por las palabras
    for fr in frases:
        if len(fr)!=0: 
            words_sw = word_tokenize(fr)
            words=[]
            for i in words_sw:
                
                if i in frec_words.keys():
                    words.append(i)

            if len(words)!=0:            
                output.append(words)

    return output





def save_dict():
    outfile = open(name_dict,'wb')
    pickle.dump(frec_words,outfile)
    outfile.close()





