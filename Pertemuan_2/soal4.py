nilai_siswa = {
   "S01": {"nama": "Dina", "tugas": 80, "uts": 75, "uas": 85},
   "S02": {"nama": "Abdul Harris", "tugas": 90, "uts": 88, "uas": 92},
   "S03": {"nama": "Sheila", "tugas": 70, "uts": 65, "uas": 70}
}

#soal 1
S04 = {'nama' : 'Fafa', 'tugas' : 85, 'uts' : 80, 'uas' : 90,}

nilai_siswa.update({"S04": S04})

#soal 2
for x in nilai_siswa.values() :
   total = (x['tugas'] * 20/100) + (x['uts'] * 30/100) + (x['uas'] * 50/100)
   #soal 3
   if total > 80 :
      print(f'{x['nama']} : nilai = {total}')