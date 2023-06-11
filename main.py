from car import Concessionaria
from database import Database
from carCLI import CarCLI
from carCRUD import CarCRUD

# Substitua por suas credenciais do banco de dados
db = Database(uri="bolt://44.214.180.5:7687", user="neo4j", password="instructor-morphine-mirrors")

car_crud = CarCRUD(db)
concessionaria = Concessionaria("Concessionária Sr. Dito")
cli = CarCLI(car_crud, concessionaria)

cli.run()