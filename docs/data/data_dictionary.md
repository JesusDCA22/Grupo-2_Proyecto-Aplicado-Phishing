# Diccionario de datos - Web page Phishing Detection Dataset

## Base de datos: URL Phishing Features

**Descripción**: Dataset que contiene 11,430 URLs etiquetadas como phishing o legítimas, con 87 características extraídas de cada URL. Las características provienen de: estructura/sintaxis de URLs (56), contenido de páginas (24) y consultas a servicios externos (7). El dataset está balanceado (50% phishing, 50% legítimo).

Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos
-------- | ----------- | ------------ | ---------------------- | --------------
url | URL completa | string | - | Extracción directa
length_url | Longitud total de la URL | integer | 1-2000 | Extracción de estructura
length_hostname | Longitud del nombre de host | integer | 1-253 | Extracción de estructura
ip | Si la URL contiene dirección IP | binary | 0 (no), 1 (sí) | Extracción de estructura
nb_dots | Número de puntos en la URL | integer | 0-10 | Extracción de estructura
nb_hyphens | Número de guiones en la URL | integer | 0-10 | Extracción de estructura
nb_at | Número de símbolos '@' | integer | 0-1 | Extracción de estructura
nb_qm | Número de signos de interrogación | integer | 0-10 | Extracción de estructura
nb_and | Número de símbolos '&' | integer | 0-10 | Extracción de estructura
nb_or | Número de símbolos '\|' | integer | 0-1 | Extracción de estructura
nb_eq | Número de signos igual '=' | integer | 0-10 | Extracción de estructura
nb_underscore | Número de guiones bajos | integer | 0-10 | Extracción de estructura
nb_tilde | Número de tildes '~' | integer | 0-1 | Extracción de estructura
nb_percent | Número de signos porcentaje | integer | 0-10 | Extracción de estructura
nb_slash | Número de barras inclinadas | integer | 0-50 | Extracción de estructura
nb_star | Número de asteriscos | integer | 0-1 | Extracción de estructura
nb_colon | Número de dos puntos | integer | 0-10 | Extracción de estructura
nb_comma | Número de comas | integer | 0-1 | Extracción de estructura
nb_semicolumn | Número de punto y coma | integer | 0-1 | Extracción de estructura
nb_dollar | Número de signos de dólar | integer | 0-1 | Extracción de estructura
nb_space | Número de espacios | integer | 0-1 | Extracción de estructura
nb_www | Número de 'www' | integer | 0-1 | Extracción de estructura
nb_com | Número de '.com' | integer | 0-1 | Extracción de estructura
nb_dslash | Número de dobles barras | integer | 0-1 | Extracción de estructura
http_in_path | Presencia de 'http' en la ruta | binary | 0 (no), 1 (sí) | Extracción de estructura
https_token | Uso de HTTPS | binary | 0 (no), 1 (sí) | Extracción de estructura
ratio_digits_url | Ratio de dígitos en la URL | float | 0.0-1.0 | Extracción de estructura
ratio_digits_host | Ratio de dígitos en el host | float | 0.0-1.0 | Extracción de estructura
punycode | Uso de codificación punycode | binary | 0 (no), 1 (sí) | Extracción de estructura
port | Puerto utilizado | integer | -1 (no especificado), 1-65535 | Extracción de estructura
tld_in_path | TLD aparece en la ruta | binary | 0 (no), 1 (sí) | Extracción de estructura
tld_in_subdomain | TLD aparece en subdominio | binary | 0 (no), 1 (sí) | Extracción de estructura
abnormal_subdomain | Subdominio anormal | binary | 0 (no), 1 (sí) | Extracción de estructura
nb_subdomains | Número de subdominios | integer | 1-10 | Extracción de estructura
prefix_suffix | Uso de prefijo/sufijo | binary | 0 (no), 1 (sí) | Extracción de estructura
random_domain | Dominio aleatorio | binary | 0 (no), 1 (sí) | Extracción de estructura
shortening_service | Uso de servicio de acortamiento | binary | 0 (no), 1 (sí) | Extracción de estructura
path_extension | Extensión en la ruta | binary | 0 (no), 1 (sí) | Extracción de estructura
nb_redirection | Número de redirecciones | integer | 0-10 | Extracción de contenido
nb_external_redirection | Número de redirecciones externas | integer | 0-10 | Extracción de contenido
length_words_raw | Longitud de palabras en URL | integer | 1-50 | Extracción de contenido
char_repeat | Caracteres repetidos | integer | 0-10 | Extracción de contenido
shortest_words_raw | Longitud de palabra más corta | integer | 1-20 | Extracción de contenido
shortest_word_host | Palabra más corta en host | integer | 1-20 | Extracción de contenido
shortest_word_path | Palabra más corta en ruta | integer | 0-20 | Extracción de contenido
longest_words_raw | Longitud de palabra más larga | integer | 1-50 | Extracción de contenido
longest_word_host | Palabra más larga en host | integer | 1-50 | Extracción de contenido
longest_word_path | Palabra más larga en ruta | integer | 0-50 | Extracción de contenido
avg_words_raw | Longitud promedio de palabras | float | 1.0-20.0 | Extracción de contenido
avg_word_host | Longitud promedio en host | float | 1.0-20.0 | Extracción de contenido
avg_word_path | Longitud promedio en ruta | float | 0.0-20.0 | Extracción de contenido
phish_hints | Términos de phishing | integer | 0-5 | Extracción de contenido
domain_in_brand | Dominio en marcas conocidas | binary | 0 (no), 1 (sí) | Extracción de contenido
brand_in_subdomain | Marca en subdominio | binary | 0 (no), 1 (sí) | Extracción de contenido
brand_in_path | Marca en ruta | binary | 0 (no), 1 (sí) | Extracción de contenido
suspecious_tld | TLD sospechoso | binary | 0 (no), 1 (sí) | Extracción de contenido
statistical_report | Reporte estadístico | binary | 0 (no), 1 (sí) | Extracción de contenido
nb_hyperlinks | Número de hipervínculos | integer | 0-500 | Extracción de contenido
ratio_intHyperlinks | Ratio de hipervínculos internos | float | 0.0-1.0 | Extracción de contenido
ratio_extHyperlinks | Ratio de hipervínculos externos | float | 0.0-1.0 | Extracción de contenido
ratio_nullHyperlinks | Ratio de hipervínculos nulos | float | 0.0-1.0 | Extracción de contenido
nb_extCSS | Número de CSS externos | integer | 0-50 | Extracción de contenido
ratio_intRedirection | Ratio de redirecciones internas | float | 0.0-1.0 | Extracción de contenido
ratio_extRedirection | Ratio de redirecciones externas | float | 0.0-1.0 | Extracción de contenido
ratio_intErrors | Ratio de errores internos | float | 0.0-1.0 | Extracción de contenido
ratio_extErrors | Ratio de errores externos | float | 0.0-1.0 | Extracción de contenido
login_form | Presencia de formulario de login | binary | 0 (no), 1 (sí) | Extracción de contenido
external_favicon | Favicon externo | binary | 0 (no), 1 (sí) | Extracción de contenido
links_in_tags | Links en tags HTML | float | 0.0-100.0 | Extracción de contenido
submit_email | Formulario que envía email | binary | 0 (no), 1 (sí) | Extracción de contenido
ratio_intMedia | Ratio de media interna | float | 0.0-100.0 | Extracción de contenido
ratio_extMedia | Ratio de media externa | float | 0.0-100.0 | Extracción de contenido
sfh | Formulario vacío o inválido | binary | 0 (no), 1 (sí) | Extracción de contenido
iframe | Uso de iframe | binary | 0 (no), 1 (sí) | Extracción de contenido
popup_window | Ventanas popup | binary | 0 (no), 1 (sí) | Extracción de contenido
safe_anchor | Anclas seguras | float | 0.0-100.0 | Extracción de contenido
onmouseover | Evento onmouseover | binary | 0 (no), 1 (sí) | Extracción de contenido
right_clic | Click derecho deshabilitado | binary | 0 (no), 1 (sí) | Extracción de contenido
empty_title | Título vacío | binary | 0 (no), 1 (sí) | Extracción de contenido
domain_in_title | Dominio en título | binary | 0 (no), 1 (sí) | Extracción de contenido
domain_with_copyright | Dominio con copyright | binary | 0 (no), 1 (sí) | Extracción de contenido
whois_registered_domain | Dominio registrado en WHOIS | binary | 0 (no), 1 (sí) | Consulta externa
domain_registration_length | Duración registro dominio | integer | -1 (desconocido), 1-10000 | Consulta externa
domain_age | Edad del dominio en días | integer | -1 (desconocido), 0-20000 | Consulta externa
web_traffic | Tráfico web | integer | -1 (desconocido), 0-1000000 | Consulta externa
dns_record | Registro DNS | binary | 0 (no), 1 (sí) | Consulta externa
google_index | Indexado en Google | binary | 0 (no), 1 (sí) | Consulta externa
page_rank | PageRank de Google | integer | -1 (desconocido), 0-10 | Consulta externa
status | Etiqueta de clase | categorical | "phishing", "legitimate" | Etiquetado manual

**Fuente original**: Hannousse, Abdelhakim; Yahiouche, Salima (2021), "Web page phishing detection", Mendeley Data, V3, doi: 10.17632/c2gw7fy2j4.3
