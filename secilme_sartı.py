#cumhurbaşkanlığı seçilme şartları
türk_vatandasi = True
if türk_vatandasi == True:
    print("Bir sonraki şart.")
else:
    print("Bu işlem için Türk vatandaşı olmanız gerekiyor.")

yas = 45
if yas >= 40:
    print("Bir sonraki şart.")
else:
    print("Yaş şartı sağlanamıyor.")

egitim_durumu = "yükseköğrenim"
if egitim_durumu == "yükseköğrenim":
    print("Bir sonraki şart.")
else:
    print("Eğitim şartı sağlanamıyor.")

zorunlu_askerlik = True
if zorunlu_askerlik == True:
    print("Bir sonraki şart.")
else:
    print("Askerlik şartı sağalanamıyor.")

oy_oranı = 52
if oy_oranı >= 50:
    print("Cumhurbaşkanı olmaya hak kazandınız.")
else:
    print("Cumhurbaşkanı olma şartını karşılayamadınız.")




#Milletvekili seçilme şartları 
vatandaslık = "Türkiye Cumhuriyeti"
if vatandaslık == "Türkiye Cumhuriyeti":
    print("Bir sonraki adım.")
else:
    print("Vatandaşlık şartını sağlayamadınız.")

yas_sınırı = 19
if yas_sınırı >= 18:
    print("Bir sonraki adım.")
else:
    print("Yaş sınırı şartını sağlayamdınız.")

egitim_durumu = "lise"
if egitim_durumu >= "ilkokul":
    print("Bir sonraki adım.")
else:
    print("Eğitim düzeyiniz şartı sağlamıyor.")

adli_sicil = "Temiz" 
if adli_sicil == "Temiz":
    print("Bir sonraki adım.")
else:
    print("Adli sicil şartını sağlayamadınız.")

askerlik_durumu = False
if askerlik_durumu == True:
    print("Milletvekili olmaya hak kazandınız.")
else:
    print("Milletvekili olamaya hak kazanamadınız")


milletvekili = False
if milletvekili == True:
    print("Cumhurbaşkanı adayı olabilirsiniz.")
else:
    print("Mlletvekili olmadığınız için cumhurbaşkanı adayı olamazsınız.")