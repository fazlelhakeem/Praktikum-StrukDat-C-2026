tim_frontend = {"HTML", "CSS", "JavaScript", "React"}
tim_backend = {"Python", "JavaScript", "SQL",
"NodeJS"}

#soal 1
keahlian_dua = tim_frontend.intersection(tim_backend)

#soal 2
keahlian_backend = tim_backend.difference(tim_frontend)

#soal 3
total = tim_frontend.union(tim_backend)