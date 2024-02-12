meme_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Laugh Out Loud, Komik bir şeye verilen cevap",
    "BRUH": "normal dışı bir şey için denilen cevap",
    }
    
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("üzgünüz, ama bu sözcük süzlüğümüzde değil")
