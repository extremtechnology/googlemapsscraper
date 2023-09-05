# Ruta absoluta al archivo queries.txt
path_to_queries_txt = "C:\\Users\\piriz\\Downloads\\google-maps-scraper-master\\google-maps-scraper-master\\src\\queries.txt"

# Leer consultas desde un archivo .txt
queries = []
with open(path_to_queries_txt, "r", encoding="utf-8") as f:
    for line in f.readlines():
        keyword, max_results = line.strip().split(",")
        queries.append({
            "keyword": keyword,
            "max_results": int(max_results),
        })

# Configuración adicional
number_of_scrapers = 6

