from openai import OpenAI



def cehckAddress(candidateAddress,documentAddress):
    prompt = f"""
    Tienes el siguiente texto extraido de un documento de identificación de domicilio busca el contenido de elementos como calle, codigo postal, ciudad, estado:
    "{documentAddress}"
    Y por otro lado otro texto de el Candidato (que es una persona) el cual indicó que su dirección es:
    "{candidateAddress}"

    Analiza los 2 elementos por separado para encontrar calle, ciudad, codigo postal, estado y en base a el resultado de cada elemento, compararlos.
    Te voy a determinar un conjunto de puntos que determinan la coincidencia entre ambos contenidos (Ten en cuenta que para sumar puntos se debe coincidir con los elementos
    del primer texto con el segundo, si la informacion no coincide entre ambos no debes otorgar puntos): 
    coincidir nombre de calle y numero - 3 puntos
    coincidir ciudad y estado - 1 punto
    coincidir codigo postal - 2 punto
    coincidir referencias - 1 punto
    cualquier combinacion debe sumar los puntos
    Devuelve:
    - MATCH si el total de puntos es 5 o mas
    - NO MATCH  si el total de puntos es 4 o menos
    - Indica el total de puntos y que fue lo que no lograste coincidir
"""
    result = client.chat.completions.create(
        model="gpt-5.4",
        messages=[{"role": "user", "content":prompt}]
    )
    return result.choices[0].message.content.strip()
    