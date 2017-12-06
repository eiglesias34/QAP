datos=read.csv("time.csv",header=TRUE)
attach(datos) 

boxplot(datos, ylab = "Tiempo",xlab = "Metaheurística", main = "Tiempo")

datos=read.csv("error.csv",header=TRUE)
attach(datos) 

boxplot(datos, ylab = "Error",xlab = "Metaheurística", main = "Error")
