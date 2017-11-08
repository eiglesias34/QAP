datos=read.csv("tiempo.csv",header=TRUE)
attach(datos) 

boxplot(datos, ylab = "Tiempo",xlab = "Metaheurística", main = "Metaheurísticas de trayectoria para QAP - Tiempo")

datos=read.csv("error.csv",header=TRUE)
attach(datos) 

boxplot(datos, ylab = "Error",xlab = "Metaheurística", main = "Metaheurísticas de trayectoria para QAP - Error")
