# Proyecto: Data-Driven-LPF

*Este repositorio contiene el desarrollo de una infraestructura de datos robusta para el análisis estadístico de la Primera División del Fútbol Argentino. El objetivo es centralizar información histórica y en tiempo real para generar insights sobre el rendimiento de equipos, jugadores y tendencias tácticas en nuestra liga.*

## Descripción del Proyecto

*El proyecto busca resolver la fragmentación de datos en el fútbol local, construyendo una base de datos relacional que permita consultas complejas y visualizaciones dinámicas. Se enfoca en métricas de rendimiento, gestión de planteles y el análisis de la tabla de promedios.*

## Stack Tecnológico
- **Lenguaje:** *Python*
- **Base de Datos:** *SQL*
- **Librerías:** Pandas, NumPy
- **ETL:** *BeautifulSoup / Selenium (Web Scraping) o integración con APIs deportivas.*
- **Visualización:** *Power BI*

## Estructura de la Base de Datos
*El modelo de datos está diseñado bajo una arquitectura relacional (Esquema Estrella/Copo de Nieve) que incluye:*
- **Equipos:** *Información institucional y estadios.*
- **Jugadores:** *Perfiles técnicos, posiciones y valores de mercado.*
- **Partidos:** *Resultados detallados, fechas y localías.*
- **Estadísticas Avanzadas:** *Pases, remates, xG (Goles Esperados) y métricas físicas.*
