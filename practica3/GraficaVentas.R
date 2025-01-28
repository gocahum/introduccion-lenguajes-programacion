# Primero, asegúrate de que el paquete ggplot2 esté instalado, en caso de que no esté, lo instala
if (!require(ggplot2)) {
  install.packages("ggplot2")
  library(ggplot2)
}
  
#Carga el archivo csv a la variable datos
datos <- read.csv(file = "sales_metrics_by_region.csv")

#Se imprimen las primeras 5 lienas para comprobar que se pudo leer el archivo
head(datos, 5)

# Crear un gráfico de barras del promedio de ventas agrupado por mes y región, utilizando la librería ggplot
sales_plot <- ggplot(datos, aes(x = Month, y = Sale_Amount, fill = Geography)) +
  stat_summary(fun = mean, geom = "bar", position = "dodge") +
  #Se agrega el titulo de la grafica
  labs(title = "Promedio de ventas por mes y region",
  #Se agrega el nombre que estará en el eje de las X que en este caso será el mes
       x = "Mes",
       #En el eje Y se agrega la etiqueta que es el promedio de ventas
       y = "Promedio de ventas",
       #Se agrega la etiqueta Region
       fill = "Region") +
  theme_minimal() +
  theme(
    plot.title = element_text(hjust = 0.5, size = 14),
    axis.title.x = element_text(size = 12),
    axis.title.y = element_text(size = 12),
    legend.title = element_text(size = 12)
  )
# Guardar el gráfico como un archivo de imagen png
ggsave("sales_metrics_plot.png", plot = sales_plot, width = 10, height = 6)
# Guardar el gráfico como un archivo de imagen pdf (la imagen png se genera sin fondo, por lo cual se ve de mala calidad)
ggsave("sales_metrics_plot.pdf", plot = sales_plot, width = 10, height = 6)