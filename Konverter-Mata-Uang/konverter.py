from kurs import kurs

def konversi(dari, ke, nilai):
   if dari == ke:
      return nilai
   elif dari == 'IDR':
      return nilai / kurs[ke]
   elif ke == 'IDR':
      return nilai * kurs[dari]
      